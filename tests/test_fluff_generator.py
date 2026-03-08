# import src.fluff_generator as fluff_generator
# import pytest
# import streamlit as st
# import streamlit.testing.v1 as st_testing


# def test_fluff_generator():
#     at = st_testing.AppTest.from_file("src/fluff_generator.py")
#     at.run()
#     assert not at.exception

import pytest
from streamlit.testing.v1 import AppTest
from unittest.mock import MagicMock, patch
import src.fluff_generator as fluff_generator


def test_app_initialization():
    """Test that the app loads and initializes the chat history."""
    at = AppTest.from_file("fluff_generator.py").run()
    
    # Check that the title is correct
    assert at.title[0].value == "Warhammer 40k Story Generator"
    
    # Check that the session state initialized the 2 default messages
    # (system_message and ai_message)
    assert len(at.session_state.messages) == 2

@patch("model_funcs.gemini_model")
@patch("retrieval.extract_relevant_history")
def test_user_input_triggers_llm(mock_retrieval, mock_model_func):
    """Test that typing in chat_input triggers the RAG and LLM logic."""
    
    # 1. Setup Mocks
    mock_retrieval.return_value = "The Ultramarines are defending Ultramar."
    
    mock_model = MagicMock()
    mock_response = MagicMock()
    mock_response.content = "For the Emperor!"
    mock_model.invoke.return_value = mock_response
    mock_model_func.return_value = mock_model

    # 2. Start the App
    at = AppTest.from_file("fluff_generator.py").run()

    # 3. Simulate user typing into the chat input
    at.chat_input[0].set_value("A new battle report: Orks vs Humans").run()

    # 4. Assertions
    # Check if retrieval was called with our input
    mock_retrieval.assert_called_with("A new battle report: Orks vs Humans")
    
    # Check if the UI updated with the AI response
    # (Note: index might vary based on your UI layout)
    assert "For the Emperor!" in at.markdown[1].value 
    
    # Check if message was added to session state
    # 2 initial + 1 user + 1 assistant = 4
    assert len(at.session_state.messages) == 4

def test_error_handling_ui(mock_model_func):
    """Test that the app shows an error message if the model fails."""
    mock_model = MagicMock()
    mock_model.invoke.side_effect = Exception("Chaos Corruption (API Error)")
    mock_model_func.return_value = mock_model
    
    at = AppTest.from_file("fluff_generator.py").run()
    at.chat_input[0].set_value("Test Error").run()
    
    # Check that the error element appeared in the UI
    assert len(at.error) > 0
    assert "Chaos Corruption" in at.error[0].value

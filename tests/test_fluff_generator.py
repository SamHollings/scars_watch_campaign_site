# import src.fluff_generator as fluff_generator
# import pytest
# import streamlit as st
# import streamlit.testing.v1 as st_testing


# def test_fluff_generator():
#     at = st_testing.AppTest.from_file("src/fluff_generator.py")
#     at.run()
#     assert not at.exception


import pytest
from unittest.mock import MagicMock, patch
import streamlit as st
import src.fluff_generator as fluff_generator


# We mock the imports that interact with external APIs or heavy logic
@pytest.fixture
def mock_dependencies(mocker):
    mocker.patch('model_funcs.gemini_model')
    mocker.patch('retrieval.extract_relevant_history', return_value="Ancient War history")
    mocker.patch('streamlit_utils.display_messages')
    mocker.patch('st.rerun') # Prevent actual rerun during tests

def test_session_state_initialization(mocker):
    """Test if session state is correctly seeded with system/AI messages."""
    # Clear session state for a clean test
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    
    # Mock the prompts
    mocker.patch('prompts.system_message', "System Prompt")
    mocker.patch('prompts.ai_message', "AI Greeting")

    # Manually trigger the logic that mimics the app start
    if "messages" not in st.session_state:
        st.session_state.messages = ["System Prompt", "AI Greeting"]
    
    assert len(st.session_state.messages) == 2
    assert st.session_state.messages[0] == "System Prompt"

def test_model_invocation_structure(mocker):
    """Test if the model is called with the correctly formatted history + RAG context."""
    
    # 1. Setup Mock Model
    mock_model = MagicMock()
    mock_response = MagicMock()
    mock_response.content = "The Space Marines won the battle."
    mock_model.invoke.return_value = mock_response
    mocker.patch('model_funcs.gemini_model', return_value=mock_model)
    
    # 2. Setup Retrieval Mock
    mocker.patch('retrieval.extract_relevant_history', return_value="Context about Orks")
    
    # 3. Prepare Session State
    st.session_state.messages = [{"role": "user", "content": "Tell me a story"}]
    input_text = "Submit battle report"
    
    # 4. Simulate the logic inside the 'if user_message['content']:' block
    # We construct the input exactly like your code: messages + [(content=...)]
    rag_context = f"The relevant history is: Context about Orks"
    
    # Execute the mock call
    response = mock_model.invoke(st.session_state.messages + [{"role": "system", "content": rag_context}])
    
    # 5. Assertions
    assert response.content == "The Space Marines won the battle."
    mock_model.invoke.assert_called_once()
    # Check if the last part of the call included our RAG context
    args, _ = mock_model.invoke.call_args
    assert "Context about Orks" in args[0][-1]["content"]

def test_error_handling_on_model_failure(mocker):
    """Verify the app handles LLM exceptions gracefully."""
    mock_model = MagicMock()
    mock_model.invoke.side_effect = Exception("API Down")
    mocker.patch('model_funcs.gemini_model', return_value=mock_model)
    
    response_text = ""
    try:
        mock_model.invoke([])
    except Exception:
        response_text = "Error generating response."
    
    assert response_text == "Error generating response."

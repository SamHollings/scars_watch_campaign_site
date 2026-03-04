import src.model_funcs as mf
import pytest

def test_gemini_model():
    model = mf.gemini_model()
    model.max_output_tokens = 10
    response = model.invoke("Test")
    assert response is not None
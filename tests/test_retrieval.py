import src.retrieval as retrieval
import pytest

def test_extract_relevant_history():
    result = retrieval.extract_relevant_history("test input")
    assert result is not None
    assert len(result) > 0
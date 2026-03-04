import src.fluff_generator as fluff_generator
import pytest
import streamlit as st
import streamlit.testing.v1 as st_testing


def test_fluff_generator():
    at = st_testing.AppTest.from_file("src/fluff_generator.py")
    at.run()
    assert not at.exception


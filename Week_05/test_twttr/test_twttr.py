import pytest
from twttr import shorten

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("1") == "1"
    assert shorten("twitter,") == "twttr,"

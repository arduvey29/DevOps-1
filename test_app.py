from app import info, phone
import pytest

def test_info():
    assert info() == "This is the info page."

def test_phone():
    assert phone() == "This is the phone page."
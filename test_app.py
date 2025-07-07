from app import info, phone, contact, about, help, home
import pytest

def test_info():
    assert info() == "Heyy!! This is the info page."

def test_phone():
    assert phone() == "This is the phone page."

def test_contact():
    assert contact() == "This is the contact page."

def test_about():
    assert about() == "This is the about page."

def test_help():
    assert help() == "This is the help page."

def test_home():
    assert home() == "Welcome to the Home Page!"
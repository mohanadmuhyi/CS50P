from working import convert
from pytest import raises

def test_error():
    with raises(ValueError):
        convert("9 AM - 5 PM")

def test_mins():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_correct():
    assert convert("9:00 AM to 5:30 PM") == "09:00 to 17:30"

def test_range():
    with raises(ValueError):
        convert("13:60 AM to 5:60 PM")

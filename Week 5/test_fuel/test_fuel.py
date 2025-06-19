from fuel import gauge, convert
from pytest import raises

def test_convert():
    assert convert("3/4") == 75
def test_gauge():
    assert gauge(1) == "E"
    assert gauge(75) == "75%"
    assert gauge(99) == "F"
def test_exp():
    with raises(ValueError):
        convert("cat/dog")
    with raises(ZeroDivisionError):
        convert("2/0")
    with raises(ValueError):
        convert("4/3")

from plates import is_valid

def test_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False
def test_first():
    assert is_valid("1FG") == False
    assert is_valid("F1") == False
def test_punc():
    assert is_valid("ABC.") == False
    assert is_valid("AB C") == False
def test_number():
    assert is_valid("AB1C") == False
    assert is_valid("AB1CE") == False
    assert is_valid("ABC1E") == False
    assert is_valid("ABC1DE") == False
    assert is_valid("ABCD1E") == False
    assert is_valid("AB1CDE") == False
def test_zero():
    assert is_valid("AB0") == False
    assert is_valid("ABC0") == False
    assert is_valid("ABCD0") == False
    assert is_valid("ABCDE0") == False

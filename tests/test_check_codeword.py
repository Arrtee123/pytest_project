from lib.check_codeword import *

def test_check_codeword_horse():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_check_codeword_house():
    result = check_codeword("house")
    assert result == "Close, but nope."

def test_check_codeword_haunt():
    result = check_codeword("haunt")
    assert result == "WRONG!"

def test_check_codeword_close():
    result = check_codeword("close")
    assert result == "WRONG!"

def test_check_codeword_enchanter():
    result = check_codeword("enchanter")
    assert result == "WRONG!"



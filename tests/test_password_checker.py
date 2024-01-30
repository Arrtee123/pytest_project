import pytest
from lib.password_checker import *

def test_empty_string_is_returned():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check("")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters"

def test_short_string_is_returned():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check("smile")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters"

def test_eight_letter_string_is_returned():
    password = PasswordChecker()
    assert password.check("shambles") == True

def test_ten_letter_string_is_returned():
    password = PasswordChecker()
    assert password.check("shambles12") == True

def test_string_with_whitespace_is_returned():
    password = PasswordChecker()
    assert password.check("shamb les") == True

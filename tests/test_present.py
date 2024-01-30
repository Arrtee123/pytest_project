import pytest
from lib.present import *

def test_wrap_one_present():
    present = Present()
    present.wrap("doll")
    assert present.unwrap() == "doll"
    
    

def test_exception_no_contents():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."


def test_wrap_two_presents():
    present = Present()
    present.wrap("doll")
    with pytest.raises(Exception) as e:
         present.wrap("car")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

def test_wrap_two_presents_preserve_first_item():
    present = Present()
    present.wrap("doll")
    with pytest.raises(Exception) as e:
         present.wrap("car")
    assert present.unwrap() == "doll"
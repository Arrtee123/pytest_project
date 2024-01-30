from lib.greet import *

def test_greet_brian():
    result = greet("Brian")
    assert result == 'Hello, Brian!'
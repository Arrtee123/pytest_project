from lib.string_builder import *

# initially output is an empty string
def test_empty_string():
    string_builder = StringBuilder()
    assert string_builder.output() == ""

def test_string_builder_hello_output():
    string = StringBuilder()
    string.add("Hello")
    assert string.output() == "Hello"

def test_string_builder_hello_length():
    string = StringBuilder()
    string.add("Hello")
    assert string.size() == 5
   

def test_string_builder_complex():
    string = StringBuilder()
    string.add("Hello what is your name?")
    result = string.size()
    assert result == 24
    result2 = string.output()
    assert result2 == "Hello what is your name?"


    # When we add multiple strings the output is concatenated

def test_adding_multiple_strings_outputs_concatenated_strings():
    string = StringBuilder()
    string.add("Hello")
    string.add(" ")
    string.add("World")
    result = string.output()
    assert result == "Hello World"

def test_adding_multiple_strings_length():
    string = StringBuilder()
    string.add("Hello")
    string.add(" ")
    string.add("World")
    assert string.size() == 11
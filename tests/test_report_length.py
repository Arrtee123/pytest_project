from lib.report_length import *

def test_length_house():
    result = report_length("house")
    assert "This string was 5 characters long"

def test_length_with_numbers():
    result = report_length("23desktop23")
    assert "This string was 11 characters long"

def test_length_with_symbols():
    result = report_length("23desk&top23")
    assert "This string was 12 characters long"

def test_length_with_spaces():
    result = report_length("23desk top23")
    assert "This string was 12 characters long"
from lib.counter import *

#  Initially reports a count of zero
def test_counter_initially_reports_zero():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."


def test_count_to_five():
    counter = Counter()
    counter.add(5)
    result = counter.report()
    assert result == "Counted to 5 so far."

    # adding multiple numbers to the count

def test_multiple_numbers_to_count():
    counter = Counter()
    counter.add(5)
    counter.add(3)
    result = counter.report()
    assert result == "Counted to 8 so far."  

def test_multiple_minus_numbers_to_count():
    counter = Counter()
    counter.add(-5)
    counter.add(-3)
    result = counter.report()
    assert result == "Counted to -8 so far."  
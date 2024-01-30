from lib.gratitudes import *

def test_initial_empty_list():
    gratitude = Gratitudes()
    assert gratitude.format() == "Be grateful for: "

def test_one_gratitude():
    gratitude = Gratitudes()
    gratitude.add('the lovely weather we are having')
    assert gratitude.format() == "Be grateful for: the lovely weather we are having"

def test_multiple_gratitudes():
    gratitude = Gratitudes()
    gratitude.add('the lovely weather')
    gratitude.add('delicious food')
    gratitude.add('good company')
    assert gratitude.format() == "Be grateful for: the lovely weather, delicious food, good company"
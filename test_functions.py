from classes import *

def test_stock():
    obj = Stock()
    assert type(obj.ingredients) == dict
    assert type(obj.display('Tea')) == bool


def test_showmenu():
    obj = ShowMenu()
    assert obj.price == 6.5

test_stock()
test_showmenu()

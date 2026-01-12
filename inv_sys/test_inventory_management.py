import pytest
from inventory_management import Inventory
i=Inventory()
def test_add_stock():

    i.add_stock("AAPL", 10)  #here we are passing the item name and its quantity
def test_remove_stock():

    i.remove_stock("AAPL",25)
    assert i.stock["AAPL"] == 5  #as there were total 20 quantity of items if we remove 10 then of course 10 quantities would be left
def test_check_availability():

    assert i.check_availability("AAPL", 5) == True   #As we have 5 quantity of aapl this condition will be true




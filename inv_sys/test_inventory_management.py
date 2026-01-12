import pytest
from inventory_management import Inventory


@pytest.fixture   #here we are making this inventory funcion the fixture of our pytest
def inventory():
    i=Inventory()
    return i


def test_add_stock(inventory):  #so in each test function we are using the inventory class returned from the fixture of pytest
   inventory.add_stock("AAPL", 10)  #here we are passing the item name and its quantity
   assert inventory.stock["AAPL"] == 10
def test_remove_stock(inventory):

    inventory.remove_stock("AAPL",25)
    assert inventory.stock["AAPL"] == 5  #as there were total 20 quantity of items if we remove 10 then of course 10 quantities would be left
def test_check_availability(inventory):

    assert inventory.check_availability("AAPL", 5) == True   #As we have 5 quantity of aapl this condition will be true




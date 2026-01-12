#inorder for the pytest to test the file and function, the file and function name must start with test_
import pytest

def add_nums(a,b):
    return a*b
def test_add_nums():
    assert add_nums(1,2) == 2   #here we are asserted or we are sure that when 1 and 2 are passed into a function add_nums the output will be 3


def divide_nums(a,b):
    if b == 0:  #if the divider is 0 then we must raise the value error
        raise ValueError('Number cannot be divided by zero')
    return a/b
def test_divide_nums():
    assert divide_nums(6,2) == 3
    with pytest.raises(ValueError):
        divide_nums(6,0)
    assert divide_nums(6,0)

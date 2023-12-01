''' 
@Program: python_py_test
@Author: Donald Osgood
@Last Date: 2023-11-28 22:16:25
@Purpose:Donald Osgood
'''

def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"

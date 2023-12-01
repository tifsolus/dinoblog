''' 
@Program: pythin_test_sum2
@Author: Donald Osgood
@Last Date: 2023-11-28 22:12:07
@Purpose:Donald Osgood
'''
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    test_sum_tuple()
    print("Everything passed")

''' 
@Program: base
@Author: Donald Osgood
@Last Date: 2023-11-28 22:08:05
@Purpose:Donald Osgood
'''
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    print("Everything passed")
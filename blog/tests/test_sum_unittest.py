''' 
@Program: test_sum_unittest
@Author: Donald Osgood
@Last Date: 2023-11-28 22:14:13
@Purpose:Donald Osgood
'''
import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()

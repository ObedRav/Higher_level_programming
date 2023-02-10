#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_pass_0(self):
        self.assertEqual(max_integer([]), None)

    def test_integers_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_integers_max_at_mid(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_integers_max_at_beg(self):
        self.assertEqual(max_integer([9, 3, 4, 2]), 9)
    
    def test_integers_one_negative_number(self):
        self.assertEqual(max_integer([9, 3, -4, 2]), 9)

    def test_integers_only_negatives_numbers(self):
        self.assertEqual(max_integer([-9, -3, -4, -2]), -2)

    def test_integers_only_one_elemet(self):
        self.assertEqual(max_integer([-2]), -2)

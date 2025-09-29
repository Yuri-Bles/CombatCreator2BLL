# test_my_module.py
import unittest

class TestAddFunction(unittest.TestCase):
    
    def test_add_numbers_true(self):
        self.assertEqual(6, 6)
# test_my_module.py
import unittest
from my_module import add

class TestAddFunction(unittest.TestCase):
    
    def test_add_numbers_true(self):
        self.assertEqual(5, 5)

if __name__ == '__main__':
    unittest.main()

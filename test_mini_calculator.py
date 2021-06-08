
import unittest
from main import MyMiniCalculator

class TestMiniCalculator(unittest.TestCase):
    def test_add(self):
        add_obj = MyMiniCalculator()
        self.assertEqual(add_obj.add(1, 1), 2), "Incorrect addition. Answer should be two"

import unittest
from keliamieji import *


class TestKeliamieji(unittest.TestCase):
    def test_ar_keliamieji_true(self):
        self.assertTrue(ar_keliamieji_true(2000))
        self.assertTrue(ar_keliamieji_true(2052))
        self.assertFalse(ar_keliamieji_true(2100))


if __name__ == "__main__":
    unittest.main()

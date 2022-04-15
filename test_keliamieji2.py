import unittest
from keliamieji import *


class TestKeliamieji(unittest.TestCase):
    def test_ar_keliamieji(self):
        self.assertEqual("Keliamieji", ar_keliamieji(2000))
        self.assertEqual("Keliamieji", ar_keliamieji(2020))

    def test_ar_nekeliamieji(self):
        self.assertEqual("Nekeliamieji", ar_keliamieji(2100))


if __name__ == "__main__":
    unittest.main()

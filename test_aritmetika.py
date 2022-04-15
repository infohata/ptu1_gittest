import unittest
from aritmetika import *


class TestAritmetika(unittest.TestCase):
    def setUp(self):
        print(" \n=== NAUJAS TESTAS ===")

    def test_sudetis(self):
        print("sudetis")
        self.assertEqual(15, sudetis(10, 5))
        self.assertEqual(0, sudetis(-1, 1))
        self.assertEqual(-2, sudetis(-1, -1))

    def test_atimtis(self):
        print("atimtis")
        self.assertEqual(5, atimtis(10, 5))
        self.assertEqual(-2, atimtis(-1, 1))
        self.assertEqual(0, atimtis(-1, -1))

    def test_daugyba(self):
        print("daugyba")
        self.assertEqual(50, daugyba(10, 5))
        self.assertEqual(-1, daugyba(-1, 1))
        self.assertEqual(1, daugyba(-1, -1))

    def test_dalyba(self):
        print("dalyba")
        self.assertEqual(2, dalyba(10, 5))
        self.assertEqual(-1, dalyba(-1, 1))
        self.assertEqual(1, dalyba(-1, -1))
        self.assertEqual(2.5, dalyba(5, 2))
        # self.assertRaises(ZeroDivisionError, dalyba, 10, 0)
        with self.assertRaises(ZeroDivisionError):
            dalyba(1, 0)


if __name__ == "__main__":
    unittest.main()

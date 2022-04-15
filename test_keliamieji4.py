import unittest
from keliamieji3 import Keliamieji


class TestKeliamieji(unittest.TestCase):
    def setUp(self):
        print("setUp")
        self.objektas = Keliamieji()

    def test_tikrinti(self):
        print("tikrinti")
        self.assertTrue(self.objektas.tikrinti(2000))
        self.assertTrue(self.objektas.tikrinti(2052))
        self.assertFalse(self.objektas.tikrinti(2100))

    def test_zbelenka(self):
        print("belenkas")
        self.assertTrue(2+2 == 4)

    def test_diapazonas(self):
        print("diapazonas")
        rezultatas = self.objektas.diapazonas(1980, 2000)
        lukestis = [1980, 1984, 1988, 1992, 1996]
        self.assertEqual(lukestis, rezultatas)


if __name__ == "__main__":
    unittest.main()

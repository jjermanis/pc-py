import unittest
from challenge00 import two_to_the_n


class Challenge00Tests(unittest.TestCase):

    def test_two(self):
        self.assertEqual(two_to_the_n(2), 4)

    def test_eight(self):
        self.assertEqual(two_to_the_n(8), 256)

    def test_actual(self):
        self.assertEqual(two_to_the_n(38), 274877906944)

    def test_zero(self):
        self.assertEqual(two_to_the_n(0), 1)


if __name__ == "__main__":
    unittest.main()

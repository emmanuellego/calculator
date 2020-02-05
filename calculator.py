import math
import unittest


# Calculator definitions
def add(a, b):
    return a + b


def subtr(a, b):
    return a - b


def multi(a, b):
    return a * b


def divide(a, b):
    return a / b


def root(a):
    return math.sqrt(a)


def square(a):
    return a * a


# Unit Tests
class TestOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5, "Must be 5")

    def test_subtr(self):
        self.assertEqual(subtr(3, 2), 1, "Must be 1")

    def test_multi(self):
        self.assertEqual(multi(2, 3), 6, "Must be 6")

    def test_divide(self):
        self.assertEqual(divide(4, 2), 2, "Must be 2")

    def test_root(self):
        self.assertEqual(root(25), 5, "Must be 5")

    def square(self):
        self.assertEqual(square(2), 4, "Must be 4")


if __name__ == "__main__":
    unittest.main()

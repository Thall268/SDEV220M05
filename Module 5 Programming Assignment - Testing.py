
import unittest
from fractions import Fraction


# Custom sum() function under test
def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total


# Unit test cases using unittest
class TestSum(unittest.TestCase):

    def test_list_int(self):
        """Test that it can sum a list of integers"""
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_tuple(self):
        """Test that it can sum a tuple of integers"""
        data = (1, 2, 3)
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_float(self):
        """Test that it can sum a list of floats"""
        data = [1.0, 2.5, 3.5]
        result = sum(data)
        self.assertEqual(result, 7.0)

    def test_list_fraction(self):
        """Test that it can sum a list of fractions (expected fail for demo)"""
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)  # This will fail: actual = 9/10

    def test_bad_input(self):
        """Test that it raises TypeError for a non-iterable input"""
        with self.assertRaises(TypeError):
            sum(5)


# Execute tests when run directly
if __name__ == '__main__':
    unittest.main()

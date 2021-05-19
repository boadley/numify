from numify import numify
import unittest

# ** Tests**


class TestNumify(unittest.TestCase):

    # Test if middle spaces are ignored
    def test_middle_space(self):
        testcase = "2   k"
        expected = 2000
        self.assertEqual(numify(testcase), expected)

    # Test if the trailing alphabet if case insensitive
    def test_capitals(self):
        testcase = "30K"
        expected = 30000
        self.assertEqual(numify(testcase), expected)

    # Test if alphanumeric characters containing floats is handled correctly
    def test_float(self):
        self.assertEqual(numify("23.4k"), 23400)

    # Test if alphanumeric characters raises errors
    def test_not_alphanum(self):
        self.assertRaises(ValueError, numify, "32")

    def test_negative_alphanum_value(self):
        self.assertEqual(numify("-33.65M"), -33650000)


unittest.main()

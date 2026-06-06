import unittest

from strkit import truncate


class TruncateTest(unittest.TestCase):
    def test_short_string_unchanged(self):
        self.assertEqual(truncate("hi", 10), "hi")

    def test_exact_length_unchanged(self):
        self.assertEqual(truncate("hello", 5), "hello")


if __name__ == "__main__":
    unittest.main()

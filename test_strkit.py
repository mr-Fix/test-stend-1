import unittest

from strkit import truncate


class TruncateTest(unittest.TestCase):
    def test_short_string_unchanged(self):
        self.assertEqual(truncate("hi", 10), "hi")

    def test_exact_length_unchanged(self):
        self.assertEqual(truncate("hello", 5), "hello")

    def test_truncate_adds_ellipsis(self):
        result = truncate("hello world", 5)
        self.assertEqual(result, "hell…")
        self.assertTrue(result.endswith("…"))
        self.assertLessEqual(len(result), 5)

    def test_non_positive_max_len_returns_empty(self):
        self.assertEqual(truncate("hello", 0), "")
        self.assertEqual(truncate("hello", -3), "")


if __name__ == "__main__":
    unittest.main()

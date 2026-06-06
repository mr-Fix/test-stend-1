import unittest

from strkit import truncate


class TruncateTest(unittest.TestCase):
    def test_short_string_unchanged(self):
        self.assertEqual(truncate("hi", 10), "hi")

    def test_exact_length_unchanged(self):
        self.assertEqual(truncate("hello", 5), "hello")

    def test_truncation_adds_ellipsis(self):
        result = truncate("hello world", 8)
        self.assertTrue(result.endswith("…"))
        self.assertEqual(result, "hello w…")

    def test_result_within_max_len(self):
        s = "the quick brown fox"
        for max_len in range(1, len(s) + 5):
            result = truncate(s, max_len)
            self.assertLessEqual(len(result), max_len)

    def test_ellipsis_reserves_one_char(self):
        # When truncating, length is exactly max_len (one char is the ellipsis).
        result = truncate("abcdefgh", 4)
        self.assertEqual(len(result), 4)
        self.assertEqual(result, "abc…")

    def test_max_len_one(self):
        self.assertEqual(truncate("abcdef", 1), "…")

    def test_non_positive_max_len_returns_empty(self):
        self.assertEqual(truncate("hello", 0), "")
        self.assertEqual(truncate("hello", -3), "")

    def test_no_ellipsis_when_not_truncated(self):
        self.assertNotIn("…", truncate("short", 10))


if __name__ == "__main__":
    unittest.main()

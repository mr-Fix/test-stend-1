import unittest

from strkit import truncate


class TruncateTest(unittest.TestCase):
    def test_short_string_unchanged(self):
        self.assertEqual(truncate("hi", 10), "hi")

    def test_exact_length_unchanged(self):
        self.assertEqual(truncate("hello", 5), "hello")

    def test_truncate_adds_ellipsis(self):
        result = truncate("hello world", 5)
        self.assertEqual(result, "hell\u2026")
        self.assertTrue(result.endswith("\u2026"))
        self.assertLessEqual(len(result), 5)

    def test_non_positive_max_len_returns_empty(self):
        self.assertEqual(truncate("hello", 0), "")
        self.assertEqual(truncate("hello", -3), "")

    # ---- review additions (agent-2) ----
    def test_empty_string_returns_empty(self):
        self.assertEqual(truncate("", 5), "")

    def test_max_len_one_is_single_ellipsis(self):
        # max_len == 1 must still fit: result is exactly the ellipsis.
        self.assertEqual(truncate("abc", 1), "\u2026")
        self.assertEqual(len(truncate("abc", 1)), 1)

    def test_length_invariant_property(self):
        # For each input, max_len from 1 to len(s)+2: result never exceeds max_len.
        for s in ["", "a", "ab", "hello", "hello world", "x" * 25]:
            for max_len in range(1, len(s) + 3):
                with self.subTest(s=s, max_len=max_len):
                    result = truncate(s, max_len)
                    self.assertLessEqual(len(result), max_len)
                    if len(s) <= max_len:
                        self.assertEqual(result, s)


if __name__ == "__main__":
    unittest.main()

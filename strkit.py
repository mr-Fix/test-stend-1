"""strkit — a tiny string-utilities library."""

ELLIPSIS = "…"


def truncate(s, max_len):
    """Shorten s to at most max_len characters.

    Behaviour:
    - max_len <= 0 returns an empty string "";
    - strings already within max_len are returned unchanged;
    - longer strings are cut and get a trailing ellipsis ("…"),
      with one character reserved for it so that the result is
      always at most max_len characters long.
    """
    if max_len <= 0:
        return ""
    if len(s) <= max_len:
        return s
    return s[: max_len - 1] + ELLIPSIS

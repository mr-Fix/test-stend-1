"""strkit — a tiny string-utilities library."""


def truncate(s, max_len):
    """Shorten s to at most max_len characters.

    NOTE (see README TODO): this naive version just hard-cuts the string.
    It does not signal that truncation happened, and it misbehaves for
    non-positive max_len.
    """
    if len(s) <= max_len:
        return s
    return s[:max_len]

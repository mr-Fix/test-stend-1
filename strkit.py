"""strkit - a tiny string-utilities library."""


def truncate(s, max_len):
    """Shorten s to at most max_len characters.

    Behaviour:
      * max_len <= 0       -> returns "" (nothing fits).
      * len(s) <= max_len  -> returns s unchanged.
      * otherwise          -> truncates and appends an ellipsis ("…"),
                              reserving one character for it so the result
                              is always <= max_len characters long.
    """
    if max_len <= 0:
        return ""
    if len(s) <= max_len:
        return s
    return s[:max_len - 1] + "…"

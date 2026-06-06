# strkit

A tiny string-utilities library — used as the working repo for a Kapsula
sandbox dogfood test (an AI agent clones this, makes a change, opens a PR).

## API

- `truncate(s, max_len)` — shorten a string to at most `max_len` characters.

## Tests

```
python -m unittest -v
```

## TODO

`truncate` currently hard-cuts the string with no indication that it was
shortened, and misbehaves for non-positive `max_len`. It should:

- append a single-character ellipsis `…` when (and only when) it shortens the
  string, with the **total** result length still `≤ max_len`;
- return `""` for `max_len <= 0`.

Tests for the new behaviour are welcome.

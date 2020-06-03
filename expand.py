#!/usr/bin/env python3
"""Expand (what's intended to be a) a T-SQL expression for searching."""


def expand(text, pattern, replacement, min_count, max_count):
    """Expands \n and a single replacement with repetitions."""
    for count in range(min_count, max_count + 1):
        print(text.replace(pattern, replacement * count)
                  .replace(r'\n', "' + CHAR(10) + '")
                  .replace(r'\N', "' + CHAR(13) + CHAR(10) + '"))


if __name__ == '__main__':
    expand(text=r"OR ph.Text LIKE '%\n[`~][`~][`~]{}[^a-z\N]%'",
           pattern=r'{}',
           replacement=r'[^\n]',
           min_count=0,
           max_count=5)  # 5 is not high enough. This is just for testing.

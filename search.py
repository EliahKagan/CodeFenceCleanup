#!/usr/bin/env python3
"""Searches posts in CSV format for signs of malformed code fences."""

import csv


with open('code-fences-with-lost-text-on-the-first-line.csv', newline='') as f:
    reader = csv.reader(f)
    for _ in range(2):
        print(next(reader)[-1])

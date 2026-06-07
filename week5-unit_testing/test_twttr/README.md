# Shorten (twttr)

## Overview
Removes all vowels from a given string, simulating the style of early Twitter where characters were dropped to save space. Handles uppercase, lowercase, numbers and punctuation correctly — only vowels are removed.

## Requirements
- Python 3.10+
- No external dependencies

## Usage

    python twttr.py

Expected interaction:

    Enter word: Twitter
    Output: Twttr

## Testing

    python -m pytest test_twttr.py -v

Expected output:

    test_twttr.py::test_uppercase   PASSED
    test_twttr.py::test_lower       PASSED
    test_twttr.py::test_numbers     PASSED
    test_twttr.py::test_punctuation PASSED
    4 passed in 0.02s

## Functions

| Function | Input | Output | Description |
|----------|-------|--------|-------------|
| main() | — | — | Prompts user for input, prints shortened result |
| shorten(word) | str | str | Returns input string with all vowels removed |

## Key Concepts
- String iteration with for loop
- Character filtering with not in
- Pure function design for testability

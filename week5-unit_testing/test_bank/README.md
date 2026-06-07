# Bank

## Overview
Accepts a greeting as input and returns a dollar value based on its content.
Returns $0 for greetings starting with "hello", $20 for greetings starting
with any other "h" word, and $100 for everything else. Input is normalised
with casefold and strip before comparison so casing and whitespace do not
affect the result.

## Requirements
- Python 3.10+
- No external dependencies

## Usage

    python bank.py

Expected interaction:

    Greeting: Hello
    You receive $0

    Greeting: How are you
    You receive $20

    Greeting: Good Morning
    You receive $100

## Testing

    python -m pytest test_bank.py -v

Expected output:

    test_bank.py::test_hello          PASSED
    test_bank.py::test_h_greetings    PASSED
    test_bank.py::test_other_greetings PASSED
    3 passed in 0.02s

## Functions

| Function | Input | Output | Description |
|----------|-------|--------|-------------|
| main() | — | — | Prompts user for greeting, prints dollar value returned by value() |
| value(greet) | str | int | Normalises input and returns 0, 20, or 100 based on greeting content |

## Key Concepts
- casefold() and strip() for input normalisation inside the tested function
- startswith() for string prefix matching
- Pure function design — normalisation inside value() not main(), enabling direct unit testing
- pytest assertions without pytest.raises() — no exceptions expected

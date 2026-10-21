# Vanity Plates

## Overview
Validates a custom vehicle vanity plate string against Massachusetts rules. Returns Valid or Invalid based on five distinct rules covering length, character type, digit placement and leading zeros.

## Requirements
- Python 3.10+
- No external dependencies

## Usage

    python plates.py

Expected interaction:

    Plate: AA12
    Valid

    Plate: AA1B2
    Invalid

## Testing

    python -m pytest test_plates.py -v

Expected output:

    test_plates.py::test_len              PASSED
    test_plates.py::test_isalpha         PASSED
    test_plates.py::test_isalnum         PASSED
    test_plates.py::test_no_leading_zero PASSED
    test_plates.py::test_numbers_at_end  PASSED
    5 passed in 0.02s

## Validation Rules

| Rule | Description |
|------|-------------|
| Length | Must be 2 to 6 characters |
| First two characters | Must be letters |
| Character set | Letters and numbers only — no spaces or special characters |
| Leading zero | Numbers cannot start with 0 |
| Digit placement | Once digits begin, no letters may follow |

## Functions

| Function | Input | Output | Description |
|----------|-------|--------|-------------|
| main() | — | — | Prompts user for plate input, prints Valid or Invalid |
| is_valid(s) | str | bool | Returns True if plate meets all five rules, False otherwise |

## Key Concepts
- String methods: isalpha(), isdigit(), isalnum()
- enumerate() for index-aware iteration
- Boolean return functions
- Multi-rule validation logic

# Fuel Gauge

## Overview
Accepts a fuel level as a fraction (e.g. 3/4), converts it to a rounded percentage, and outputs E if at or below 1%, F if at or above 99%, or the percentage value otherwise. Raises exceptions on invalid input rather than silently failing.

## Requirements
- Python 3.10+
- No external dependencies

## Usage

    python fuel.py

Expected interaction:

    Enter Fuel Amount in fraction [positive integers only]: 3/4
    75%

    Enter Fuel Amount in fraction [positive integers only]: 1/100
    E

    Enter Fuel Amount in fraction [positive integers only]: 99/100
    F

## Testing

    python -m pytest test_fuel.py -v

Expected output:

    test_fuel.py::test_convert  PASSED
    test_fuel.py::test_gauge    PASSED
    2 passed in 0.02s

## Functions

| Function | Input | Output | Description |
|----------|-------|--------|-------------|
| main() | — | — | Input loop — prompts user, calls convert and gauge, prints result |
| convert(fraction) | str (X/Y format) | int | Converts fraction string to rounded percentage. Raises ValueError if X > Y or input is non-integer. Raises ZeroDivisionError if Y is 0 |
| gauge(percentage) | int | str | Returns E, F, or Z% based on percentage value |

## Error Handling

| Condition | Exception |
|-----------|-----------|
| Denominator is 0 | ZeroDivisionError |
| Numerator exceeds denominator | ValueError |
| Non-integer input | ValueError |

## Key Concepts
- Separating logic from input handling across functions
- Deliberately raising ValueError and ZeroDivisionError
- pytest.raises() for exception testing
- round() for percentage conversion
- Pure function design

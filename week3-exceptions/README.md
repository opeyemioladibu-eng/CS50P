# Week 3 — Exceptions

## Topic Summary
Exceptions are errors that occur during a program's execution. Instead of 
crashing, Python lets you catch and handle them gracefully using try/except 
blocks. This week covers handling bad user input, division errors, and 
end-of-file signals cleanly.

## Problem Sets

| File | Problem | Description |
|------|---------|-------------|
| fuel.py | Fuel Gauge | Takes fuel level as a fraction, converts to percentage. Handles ZeroDivisionError if denominator is 0 and ValueError if numerator exceeds denominator |
| taqueria.py | Felipe's Taqueria | Simulates a food ordering system for Felipe's Taqueria — takes continuous orders, returns running total, ignores invalid items, stops on EOFError |
| grocery.py | Grocery List | Accepts continuous grocery input until EOFError, then outputs items sorted alphabetically in uppercase with how many times each was entered |
| outdated.py | Outdated | Takes a date in American middle-endian format (numeric or text) and converts it to ISO 8601 international standard (YYYY-MM-DD) |

## Key Concepts
- `try` / `except` blocks
- Catching `ValueError`, `ZeroDivisionError`, `EOFError`
- `raise` to manually trigger exceptions
- Dictionary counting pattern
- `sorted()` for alphabetical ordering
- Date format conversion
- Continuous input loops with clean exit handling

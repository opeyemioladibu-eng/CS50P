# Week 8 — Object-Oriented Programming

## Topic Summary

This week covers classes, instances, properties, and operator overloading. Solutions keep data inside objects instead of passing loose values around, and tests check the class behaviour rather than printed output.

## Problem Sets

| File | Problem | Description |
|------|---------|-------------|
| cookie-jar/jar.py | Cookie Jar | A `Jar` class with capacity, deposit, withdraw, and a cookie-emoji string representation |
| seasons-of-love/seasons.py | Seasons of Love | Converts a date of birth into minutes lived, spoken in English with `inflect` |
| shirtificate/shirtificate.py | CS50 Shirtificate | Writes an A4 PDF of a CS50 shirt with the user's name using `fpdf` |

## Testing

From a problem subfolder that has tests:

```text
python -m pytest test_jar.py -v
python -m pytest test_seasons.py -v
```

## Key Concepts

- Classes, constructors, and instance methods
- `@property` for read-only attributes
- `ValueError` for invalid state
- `datetime.date` for date arithmetic
- Third-party libraries: `inflect`, `fpdf`

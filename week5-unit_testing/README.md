# Week 5 — Unit Testing

## Topic Summary
Unit testing is the practice of writing code that tests your code. This week introduces pytest as a testing framework, pylint as a static code analyser, and the discipline of writing pure, testable functions. Each problem was restructured to separate logic from input handling — making functions easier to test in isolation. PEP 8 compliance was enforced via pylint, with black used for formatting where applicable.

## Repository Structure

week5-unit_testing/
├── test_bank/
│   ├── bank.py
│   └── test_bank.py
├── twttr/
│   ├── twttr.py
│   └── test_twttr.py
├── test_plate/
│   ├── plates.py
│   └── test_plates.py
└── test_fuel/
    ├── fuel.py
    └── test_fuel.py

## Problem Sets

| File | Problem | Description |
|------|---------|-------------|
| test_bank/bank.py | Bank | Takes a greeting as input and returns a dollar value — $0 for hello, $20 for other h-greetings, $100 for everything else |
| twttr/twttr.py | Shorten | Takes a word as input and removes all vowels, simulating Twitter's old character-saving style |
| test_plate/plates.py | Vanity Plates | Validates a custom vanity plate string against five rules covering length, character type, digit placement and leading zeros |
| test_fuel/fuel.py | Fuel Gauge | Takes a fuel fraction as input, converts it to a percentage and outputs E, F, or the percentage value |

## Testing

Each problem has a dedicated test file. To run tests, cd into the problem subfolder and run:

    python -m pytest test_<problem>.py -v

Example:

    cd twttr
    python -m pytest test_twttr.py -v

## Code Quality

Static analysis was run on all test files using pylint:

    python -m pylint test_<problem>.py

All files were brought to a pylint score of 10.00/10, enforcing:
- Module and function docstrings
- PEP 8 compliant assertions (assert not x over assert x == False)
- Clean import structure

## Key Concepts
- pytest for unit testing and test discovery
- pytest.raises() for exception testing
- pylint for static code analysis and PEP 8 enforcement
- black for automated code formatting
- Writing pure functions with no side effects for testability
- Separating input handling (main()) from logic (convert(), gauge(), shorten(), value())
- Docstrings: module-level and function-level
- Raising ValueError and ZeroDivisionError deliberately
- Boolean assertions: assert not x and assert x over == False and == True

# Week 4 — Libraries

## Topic Summary
Libraries extend Python's capabilities beyond its built-in tools. This week covers importing and using third-party modules, working with command-line arguments, making live API requests, and parsing JSON responses to extract real-world data.

## Problem Sets

| File | Problem | Description |
|------|---------|-------------|
| adieu.py | Adieu | Collects names until EOF (Ctrl+D), then prints a formatted farewell using proper comma and "and" separators |
| bitcoin.py | Bitcoin Price Index | Takes a number of Bitcoins as a command-line argument and outputs the current cost in USD by querying the live CoinCap API |
| emojize.py | Emojize | Prompts user for text containing emoji aliases and outputs the emojized version using the `emoji` module |
| figlet.py | Figlet | Renders user input as ASCII art using a random or user-specified font via the `pyfiglet` module |
| game.py | Guessing Game | Generates a random number up to a user-defined level and prompts the user to guess until correct |
| professor.py | Little Professor | Generates 10 random addition problems at a chosen difficulty level, tracks score and allows up to 3 attempts per question |

## Key Concepts
- Third-party modules: `emoji`, `pyfiglet`, `requests`
- Command-line arguments with `sys.argv`
- Live API calls and JSON parsing
- Exception handling: `ValueError`, `EOFError`, `requests.RequestException`
- `random` module: `randint`, `randrange`, `choice`
- F-string formatting: thousands separator and decimal places
- Loop control with boolean flags
- Input validation with `while True` re-prompting

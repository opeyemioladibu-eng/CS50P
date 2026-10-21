# PizzaPy
## Overview
Reads a CSV file of pizza menu items and prints the contents as a neatly formatted grid table using the `tabulate` library. Validates that exactly one command-line argument is provided, that it ends in `.csv`, and that the file actually exists. The first row of the CSV is treated as the header.
## Requirements
- Python 3.10+
- tabulate
## Installation
    pip install tabulate
## Usage
    python pizza.py menu.csv
## Key Concepts
- Reading CSV files with `csv.reader`
- Pretty-printing tables with `tabulate` using `grid` format
- Command-line argument validation
- `FileNotFoundError` handling

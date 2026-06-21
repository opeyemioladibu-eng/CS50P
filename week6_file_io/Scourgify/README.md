# Scourgify
## Overview
Reads a CSV file where student names are stored as "Last, First" in a single `name` column, then rewrites the data into a new CSV with separate `first`, `last`, and `house` columns. Validates that exactly two command-line arguments are provided — input file and output file. Named after the Harry Potter spell for tidying things up.
## Requirements
- Python 3.10+
- No external dependencies
## Usage
    python scourgify.py input.csv output.csv
## Key Concepts
- Reading CSVs with `csv.DictReader`
- Writing CSVs with `csv.DictWriter`
- String splitting to reformat name columns
- Command-line argument validation

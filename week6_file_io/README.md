# Week 6 — File I/O
## Topic Summary
File I/O is about reading from and writing to files — CSVs, images, and Python source files. This week introduces Python's built-in `csv` module for structured data handling, Pillow (PIL) for image manipulation, and `tabulate` for pretty-printing tabular data. Each problem reinforces command-line argument validation via `sys.argv`, proper error handling with `try/except`, and clean separation between input validation and core logic.
## Problem Sets
| File | Problem | Description |
|------|---------|-------------|
| shirt/shirt.py | Shirt | Overlays a shirt image onto a user-supplied photo using Pillow — validates file extensions, matches input/output formats, resizes and pastes with transparency |
| pizza/pizza.py | PizzaPy | Reads a CSV file of pizza menu items and prints it as a formatted grid table using tabulate |
| scourgify/scourgify.py | Scourgify | Reads a CSV of student names in "Last, First" format and rewrites them into a new CSV with separate first, last, and house columns |
| lines/lines.py | Lines of Code | Counts the actual lines of code in a Python file — excluding blank lines and comments |
## Key Concepts
- Reading and writing CSV files with `csv.reader` and `csv.DictWriter`
- Image manipulation with Pillow: `ImageOps.fit()`, `paste()`, transparency masks
- Pretty-printing tabular data with `tabulate`
- Command-line argument validation with `sys.argv`
- `os.path.splitext()` for file extension handling
- `try/except` for graceful error handling
- `FileNotFoundError` and `sys.exit()` for clean program termination

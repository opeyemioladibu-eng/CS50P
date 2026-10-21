# Shirt
## Overview
Overlays a shirt image (`shirt.png`) onto a user-supplied photo using the Pillow library. Validates that exactly two command-line arguments are provided, that both files have matching extensions (`.jpg`, `.jpeg`, or `.png`), and that the input file actually exists. Resizes the input image to match the shirt dimensions using `ImageOps.fit()`, then pastes the shirt on top using its transparency mask.
## Requirements
- Python 3.10+
- Pillow
## Installation
    pip install Pillow
## Usage
    python shirt.py input.jpg output.jpg
## Key Concepts
- `ImageOps.fit()` for resizing while preserving aspect ratio
- `paste()` with transparency mask for clean overlay
- `os.path.splitext()` for extension extraction and comparison
- `sys.argv` for command-line argument handling

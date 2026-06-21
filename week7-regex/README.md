# Week 7 — Regular Expressions
## Topic Summary
Regular expressions (regex) are a powerful way to match, extract, and validate patterns in strings. This week introduces Python's `re` module — covering `re.search()`, `re.fullmatch()`, `re.findall()`, and key regex syntax like word boundaries (`\b`), optional groups (`?`), and character classes (`\d`, `[a-zA-Z0-9]`). Where regex wasn't required, third-party PyPI libraries were used instead — reinforcing the habit of reaching for existing tools rather than reinventing the wheel.
## Problem Sets
| File | Problem | Description |
|------|---------|-------------|
| numb3rs/numb3rs.py | NUMB3RS | Validates an IPv4 address — checks dot-decimal structure with regex and confirms each octet is between 0 and 255 |
| watch/watch.py | Watch on YouTube | Extracts a YouTube embed URL from an iframe src attribute and converts it to a shorter youtu.be link |
| working/working.py | Working 9 to 5 | Converts 12-hour time ranges to 24-hour format, handling optional minutes, AM/PM edge cases, and invalid input via ValueError |
| um/um.py | Um | Counts occurrences of the word "um" in a string, case-insensitively, ignoring substrings like "yummy" or "album" |
| response/response.py | Response | Validates an email address using the validators PyPI library — no regex, just a single function call |
## Key Concepts
- `re.fullmatch()` for exact pattern matching
- `re.search()` for finding patterns within strings
- `re.findall()` for counting all matches
- Word boundaries with `\b` to match whole words only
- Optional groups with `?`
- Capturing groups with `()` and extracting via `match.group()`
- Numeric range validation beyond what regex can handle alone
- Third-party library: `validators` for email validation

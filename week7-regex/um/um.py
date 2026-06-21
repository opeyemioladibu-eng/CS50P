import re
import sys


def main():
    user_input = str(input("Text: "))
    print(count(user_input))


def count(s):
    # find all occurrences of "um" as a whole word, case insensitive
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)
    total = len(matches)
    return total


if __name__ == "__main__":
    main()
import re
import sys


def main():
    print(parse(input("HTML:")))


def parse(html):
    match = re.search(r'src="https?://(www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"', html)
    if match:
        return f"https://youtu.be/{match.group(2)}"
    else:
        return False


if __name__ == "__main__":
    main()
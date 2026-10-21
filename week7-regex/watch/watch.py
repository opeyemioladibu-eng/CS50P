import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(html):
    # Regex ensures the pattern is matched within an iframe tag, specifically checking the src attribute
    match = re.search(r'<iframe[^>]*\bsrc=["\']https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)["\'][^>]*>', html)
    if match:
        # Added the missing forward slash after .be
        return f"https://youtu.be/{match.group(1)}"
    return None


if __name__ == "__main__":
    main()

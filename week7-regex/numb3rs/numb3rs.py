import re
import sys


def main():
    print(validate(input("IP:")))


def validate(ip):
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", ip)
    if match:
        return all(0 <= int(match.group(i)) <= 255 for i in range(1, 5))
    else:
        return False


if __name__ == "__main__":
    main()

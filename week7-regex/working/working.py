import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.fullmatch(r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)", s)
    if not match:
        raise ValueError("Invalid format")

    start_hour, start_min, start_period, end_hour, end_min, end_period = match.groups()

    start_min = int(start_min) if start_min else 0
    end_min = int(end_min) if end_min else 0
    start_hour = int(start_hour)
    end_hour = int(end_hour)

    if not (0 <= start_min <= 59) or not (0 <= end_min <= 59):
        raise ValueError("Invalid minutes")
    if not (1 <= start_hour <= 12) or not (1 <= end_hour <= 12):
        raise ValueError("Invalid hours")

    start_hour = convert_hour(start_hour, start_period)
    end_hour = convert_hour(end_hour, end_period)

    return f"{start_hour:02}:{start_min:02} to {end_hour:02}:{end_min:02}"


def convert_hour(hour, period):
    if period == "AM":
        if hour == 12:
            return 0
        return hour
    else:
        if hour == 12:
            return 12
        return hour + 12


if __name__ == "__main__":
    main()
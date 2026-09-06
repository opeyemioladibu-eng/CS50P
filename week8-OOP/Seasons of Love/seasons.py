import sys
from datetime import date
import inflect


def main():
    # Get user input and immediately try to parse it
    dob_input = input("Date of Birth: ")
    birth_date = parse_date(dob_input)

    # Calculate total minutes from birth to today
    today = date.today()
    total_minutes = calculate_minutes(birth_date, today)

    # Convert the numeric minutes into the final lyrical text
    output_text = minutes_to_text(total_minutes)
    print(output_text)


def parse_date(date_string):
    """Safely converts a string to a date object, exiting on invalid formats."""
    try:
        return date.fromisoformat(date_string)
    except ValueError:
        sys.exit("Invalid date")


def calculate_minutes(birth_date, current_date):
    """Calculates the time difference in minutes between two dates."""
    if birth_date > current_date:
        return 0

    time_delta = current_date - birth_date
    minutes_per_day = 24 * 60
    return time_delta.days * minutes_per_day


def minutes_to_text(minutes):
    """Converts a number of minutes into capitalized words without the word 'and'."""
    p = inflect.engine()
    raw_words = p.number_to_words(minutes, decimals=0)

    # Strip out any instances of 'and' to match the song style requirement
    clean_words = raw_words.replace(" and ", " ")

    return f"{clean_words.capitalize()} minutes"


if __name__ == "__main__":
    main()

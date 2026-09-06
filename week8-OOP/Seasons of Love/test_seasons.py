from datetime import date
from seasons import calculate_minutes, minutes_to_text


def test_calculate_minutes():
    # Exactly one standard day
    assert calculate_minutes(date(2025, 1, 1), date(2025, 1, 2)) == 1440

    # A standard common year gap (365 days)
    assert calculate_minutes(date(2022, 1, 1), date(2023, 1, 1)) == 525600

    # A leap year gap containing February 29th (366 days)
    assert calculate_minutes(date(2024, 1, 1), date(2025, 1, 1)) == 527040


def test_minutes_to_text():
    # Standard one-year count
    assert (
        minutes_to_text(525600)
        == "Five hundred twenty-five thousand, six hundred minutes"
    )

    # Two-year count
    assert (
        minutes_to_text(1051200)
        == "One million, fifty-one thousand, two hundred minutes"
    )

    # Short count
    assert minutes_to_text(1440) == "One thousand, four hundred forty minutes"

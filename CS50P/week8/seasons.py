from datetime import date
import inflect
import sys


def main():
    """Gets user dob and current date to calculate minute delta from dob to now"""

    p = inflect.engine()

    dob = get_dob(input("What is your date of birth in YYYY-MM-DD format: "))
    now = date.today()

    print(f"{(p.number_to_words(calculate_delta(dob, now), andword="")).capitalize()} minutes")


def get_dob(s):
    """Use fromisoformat to format user input into date-time"""

    try:
        return date.fromisoformat(s)
    except ValueError:
        sys.exit("Invalid date")


def calculate_delta(dob, now):
    """Calculates the delta from dob to now"""

    delta = now - dob
    count = round(delta.total_seconds() / 60)
    return count


if __name__ == "__main__":
    main()

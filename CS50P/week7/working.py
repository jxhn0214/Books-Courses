import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.search(
        r"(?P<first_hour>\d\d?):?(?P<first_minute>\d\d)? (?P<first_AMorPM>PM|AM) to (?P<second_hour>\d\d?):?(?P<second_minute>\d\d)? (?P<second_AMorPM>PM|AM)",
        s,
    )
    if match:
        first_hour = match.group("first_hour")
        first_minute = match.group("first_minute")
        second_hour = match.group("second_hour")
        second_minute = match.group("second_minute")

        if match.group("first_AMorPM") == "PM":
            if first_hour != "12":
                first_hour = int(first_hour)
                first_hour += 12

            if int(second_hour) < 10:
                second_hour = "0" + second_hour
            elif second_hour == "12":
                first_hour == "00"

            return print_24hrclock(first_hour, first_minute, second_hour, second_minute)

        elif match.group("second_AMorPM") == "PM":
            if second_hour != "12":
                second_hour = int(second_hour)
                second_hour += 12

            if int(first_hour) < 10:
                first_hour = "0" + first_hour
            elif first_hour == "12":
                first_hour = "00"

            return print_24hrclock(first_hour, first_minute, second_hour, second_minute)

    else:
        raise ValueError


def check_minutes(minutes):
    """Checks if minutes abide time rules"""

    minutes = int(minutes)

    if 0 <= minutes < 60:
        minutes = str(minutes)
        return minutes
    else:
        raise ValueError


def check_hours(first_hour, second_hour):
    """Checks if hours bide time rules"""

    first_hour = int(first_hour)
    second_hour = int(second_hour)

    if 0 <= first_hour < 24 and 0 <= second_hour < 24:
        first_hour = str(first_hour)
        second_hour = str(second_hour)
        return first_hour, second_hour
    else:
        raise ValueError


def print_24hrclock(first_hour, first_minute, second_hour, second_minute):
    """prints out 24 hour clock format based on availability of minutes"""

    if first_minute and not second_minute:
        check_minutes(first_minute)
        check_hours(first_hour, second_hour)
        return f"{first_hour}:{first_minute} to {second_hour}:00"
    elif second_minute and not first_minute:
        check_minutes(second_minute)
        check_hours(first_hour, second_hour)
        return f"{first_hour}:00 to {second_hour}:{second_minute}"
    elif not first_minute and not second_minute:
        check_hours(first_hour, second_hour)
        return f"{first_hour}:00 to {second_hour}:00"
    else:
        check_minutes(first_minute)
        check_minutes(second_minute)
        check_hours(first_hour, second_hour)
        return f"{first_hour}:{first_minute} to {second_hour}:{second_minute}"


if __name__ == "__main__":
    main()


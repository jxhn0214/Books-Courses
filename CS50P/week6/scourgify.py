import sys
import csv


def check_arguments():
    """Check if arguments meet requirements"""

    if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
        if len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        elif len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        else:
            return True


def organize_csv(before, after):
    """Read information from file and format/update it to a new file"""
    try:
        with open(before) as before_file, open(after, "w") as after_file:
            reader = csv.DictReader(before_file)
            writer = csv.DictWriter(after_file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in reader: # reads rows in before file and copys it into after file
                last, first = row["name"].replace(" ", "").split(",")
                house = row["house"]
                writer.writerow(
                    {
                        "first": first,
                        "last": last,
                        "house": house,
                    }
                )
    except FileNotFoundError as e:
        sys.exit(f"Could not read {e.filename}")  # Print file that could not be read


def main():
    if check_arguments():
        organize_csv(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
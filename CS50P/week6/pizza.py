import sys
from tabulate import tabulate


def check_arguments():
    """Check if sys arguments meet requirements"""

    if sys.argv[1].endswith(".csv"):
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        else:
            return True
    else:
        sys.exit("Not a CSV file")


def print_menu(csv_file): # input csv_file that you want a menu of as an argument
    """prints menu given which menu"""

    # info needed for tabulate
    headers = []
    table = []

    with open(csv_file) as file:
        lines = file.readlines()  # read csv and create empty lists for tabulate

        for word in lines[0].split(","):  # headers in italian.csv
            header = f"{word.rstrip()}"
            headers.append(header)

        for line in lines[1:]:  # body items in italian.csv
            item = line.rstrip().split(",")
            table.append(item)

        print(tabulate(table, headers, tablefmt="grid"))


def main():
    if check_arguments():
        print_menu(sys.argv[1])


if __name__ == "__main__":
    main()
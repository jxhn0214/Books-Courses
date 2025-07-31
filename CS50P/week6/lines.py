import sys

def check_arguments():
    if sys.argv[1].endswith(".py"):
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        else:
            return True
    else:
        sys.exit("Not a python file")

def num_lines():
    counter = 0
    try:
        with open(sys.argv[1]) as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line and not line.startswith("#"):
                    counter += 1
        print(counter, end="")
    except FileNotFoundError:
        sys.exit("File does not exist")


def main():
    if check_arguments():
        num_lines()


if __name__ == "__main__":
    main()
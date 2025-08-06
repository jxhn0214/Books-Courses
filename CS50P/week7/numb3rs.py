import re
import sys


def main():
    """Added sys argument support without requirements"""

    if len(sys.argv) > 1:
        print(validate(sys.argv[1]))
    else:
        print(validate(input("IPv4 Address: ")))


def validate(ip):
    """Checks to see if the ip syntax is valid"""

    sections = ip.split(".")
    match = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
    section_correct = 0

    if match:
        for section in sections:
            if 0 <= int(section) <= 255:
                if not (section[0] == "0" and len(section) > 1):
                    section_correct += 1
                else:
                    continue
            else:
                continue
    else:
        return False

    if section_correct == 4:
        return True
    else:
        return False

if __name__ == "__main__":
    main()

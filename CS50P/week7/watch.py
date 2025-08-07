import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r"<iframe.*?src=\"https?://(www\.)?youtube\.com/embed/(\w{11})?\"", s)
    if match:
        code = match.group(2)
        url = f"https://youtu.be/{code}"
        return url
    else:
        return None


if __name__ == "__main__":

    main()
import pyfiglet
import sys

fonts = ["slant", "rectangles", "alphabet"]

if len(sys.argv) == 3:
    if (sys.argv[1] == "-f") or (sys.argv[1] == "--font"):
        if sys.argv[2] not in fonts:
            raise sys.exit("Invalid Usage")
        else:
            font = sys.argv[2]
            text = input("Input: ")
            print(pyfiglet.figlet_format(text, font=font))
    else:
        raise sys.exit("Invalid Usage")
elif len(sys.argv) == 1:
    font = "standard"
    text = input("Input: ")
    print(pyfiglet.figlet_format(text, font=font))
else:
    raise sys.exit("Invalid Usage")

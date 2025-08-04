import sys
from PIL import (Image, ImageOps)


def check_arguments():
    """Check if arguments pass the requirements to use them"""

    extensions = ["jpg", "jpeg", "png"]
    muppet = sys.argv[1].strip().split(".")
    after = sys.argv[2].strip().split(".")
    muppet_extension = muppet[1]
    after_extension = after[1]

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        if muppet_extension not in extensions or after_extension not in extensions:
            sys.exit("File format not supported")
        elif muppet_extension != after_extension:
            sys.exit("File formats of the arguments do not match")
        else:
            return True


def format_picture(muppet, output):
    """Format the shit picture onto the muppet and save as after picture"""

    try:
        muppet = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
    except FileNotFoundError as e:
        sys.exit(f"could not find the file(s) {e.filename}")

    shirt_size = shirt.size #get size of shirt for fit method
    muppet = ImageOps.fit(muppet, shirt_size) #format muppet to size of shirt
    muppet.paste(shirt, shirt)
    muppet.save(output)


def main():
    if check_arguments():
        format_picture(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
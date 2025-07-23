import emoji


def main():
    user_input = input("Input: ").strip()
    print(emoji.emojize(f"{user_input}", language="alias"))


main()

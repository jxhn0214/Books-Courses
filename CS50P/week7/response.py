from validator_collection import validators, checkers, errors


def main():
    print(verify(input("What's your email address? ")))


def verify(s):
    try:
        if (email := validators.email(s)):
            return "Valid"
    except errors.InvalidEmailError:
        return "Invalid"


if __name__ == "__main__":
    main()
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) in range (2, 7):
        if s.isalpha():
            return True

        elif s[:2].isalpha():
            for char in s:
                if char.isdigit():
                    if int(char) == 0:
                        return False

                    else:
                        index = s.index(char)

                        if s[index:].isdigit():
                            return True
                        else:
                            return False

main()
def adieu_to(a):  # prints adieu to list of names while meeting grammar standards
    if len(a) == 1:
        print(a[0])
    elif len(a) == 2:
        print(f"{a[0]} and {a[1]}")
    else:
        for name in a:
            if name != a[-1]:
                print(f"{name}, ", end="")
            else:
                print(f"and {name}")


def main():
    names = []

    while True:
        try:
            names.append(input("Name: "))
        except EOFError:
            print()
            print("Adieu, adieu, to ", end="")
            adieu_to(names)
            break


main()
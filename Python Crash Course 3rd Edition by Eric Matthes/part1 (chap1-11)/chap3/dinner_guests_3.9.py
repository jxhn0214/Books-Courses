def main():
    people = ['george washington', 'andrew carneige', 'jesus']
    print(f"{people[0].title()}, would you like to have a dinner with 2 other people and myself?")
    print(f"{people[1].title()}, would you like to have a dinner with 2 other people and myself?")
    print(f"{people[-1].title()}, would you like to have a dinner with 2 other people and myself?")

    print(f"\nA total of {len(people)} are invited to the dinner.")

main()
          
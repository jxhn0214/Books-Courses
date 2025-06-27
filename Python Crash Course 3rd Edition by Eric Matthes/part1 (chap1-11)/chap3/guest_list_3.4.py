'''

If you could invite anyone, living or deceased, to dinner,
who would you invite? Make a list that includes at least three people you’d
like to invite to dinner. Then use your list to print a message to each person,
inviting them to dinner.

'''

def main():
    people = ['george washington', 'andrew carneige', 'jesus']
    print(f"{people[0].title()}, would you like to have a dinner with 2 other people and myself?")
    print(f"{people[1].title()}, would you like to have a dinner with 2 other people and myself?")
    print(f"{people[-1].title()}, would you like to have a dinner with 2 other people and myself?")

main()
          
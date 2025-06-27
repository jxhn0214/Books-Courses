'''
You just found a bigger dinner table, so now more space
is available. Think of three more guests to invite to dinner.
Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
end of your program, informing people that you found a bigger table.
Use insert() to add one new guest to the beginning of your list.
Use insert() to add one new guest to the middle of your list.
Use append() to add one new guest to the end of your list.
'''

def main():
    people = ['george washington', 'andrew carneige', 'jesus']
    print(f"{people[0].title()}, would you like to have a dinner with 2 other people and myself?")
    print(f"{people[1].title()}, would you like to have a dinner with 2 other people and myself?")
    print(f"{people[-1].title()}, would you like to have a dinner with 2 other people and myself?")

    print("\nWe found space for 3 more guests\n")

    people.insert(0, 'jason ween')
    people.insert(3, 'frank ocean')
    people.append('daniel ceaser')

    print(f"the new list of guests are {people}")

main()
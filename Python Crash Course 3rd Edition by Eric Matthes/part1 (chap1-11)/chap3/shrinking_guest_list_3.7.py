'''
You just found out that your new dinner table
won’t arrive in time for the dinner, and now you have space for only two
guests.
Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
Use pop() to remove guests from your list one at a time until only two names
remain in your list. Each time you pop a name from your list, print a
message to that person letting them know you’re sorry you can’t invite
them to dinner.
Print a message to each of the two people still on your list, letting them
know they’re still invited.
Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end of
your program.
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

    print(f"the new list of guests are {people}\n")

    print("\nUnfortunately the table has been reduced to size 3\n")

    print(f"sorry {people[-1].title()}, you have been uninvited")
    people.pop(-1)

    print(f"sorry {people[-1].title()}, you have been uninvited")
    people.pop(-1)

    print(f"sorry {people[-1].title()}, you have been uninvited")
    people.pop(-1)

    print(f"sorry {people[-1].title()}, you have been uninvited")
    people.pop(-1)

    print(f"{people[0].title()} and {people[1].title()} you both are still invited")

    del people[0]
    del people[-1]

    print(people) # check if list is empty


main()




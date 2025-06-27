'''

You just heard that one of your guests can’t
make the dinner, so you need to send out a new set of invitations. You’ll
have to think of someone else to invite.
Start with your program from Exercise 3-4. Add a print() call at the end of
your program, stating the name of the guest who can’t make it.
Modify your list, replacing the name of the guest who can’t make it with the
name of the new person you are inviting.
Print a second set of invitation messages, one for each person who is still in
your list

'''

def main():
    people = ['george washington', 'andrew carneige', 'jesus']
    print(f"{people[0].title()}, would you like to have a dinner with 2 other people and myself?")
    print(f"{people[1].title()}, would you like to have a dinner wiht 2 othe people and myself?")
    print(f"{people[-1].title()}, would you like to have a dinner with 2 other people and myself?")

    print(f"\n{people[1].title()} cannot make it\n")
    people.insert(1, 'jason')

    print(f"{people[0].title()}, would you like to have a dinner with 2 other people and myself?")
    print(f"{people[1].title()}, would you like to have a dinner wiht 2 othe people and myself?")
    print(f"{people[-1].title()}, would you like to have a dinner with 2 other people and myself?")


main()

'''
Start with the list you used in Exercise 3-1, but instead of
just printing each person’s name, print a message to them. The text of each
message should be the same, but each message should be personalized
with the person’s name.

'''

def main():
    names = ['derek', 'tristan', 'aiden', 'jeimie']
    print(f"Hi {names[0].title()}, how was your trip?")
    print(f"Hello {names[1].title()}, how are you doing?")
    print(f"Goodevening {names[-2].title()}, how was work today?")
    print(f"What's up {names[-1].title()} I haven't seen you in a long time, how is Tito?")


main()
import random

random_chars = (1, 42, 23, 5, 61, 23, 6, 14, 76, 56, 'j', 'h', 'i', 'a', 'w')
winning_chars = random.sample(random_chars, 4)
print(f"Any ticket with these matching letters/numbers wins {winning_chars}")

my_ticket =[]
counter = 0

while my_ticket != winning_chars:
    my_ticket = random.sample(random_chars, 4)

    if my_ticket != winning_chars:
        counter += 1
    else:
        print(f"It took {counter} tries to get the winning ticket")




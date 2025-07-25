import random


def main():
    while True:
        try:
            rand_limit = int(input("Level: "))
            if rand_limit < 1:
                raise ValueError
        except ValueError:
            pass
        else:
            break

    correct_answer = random.randint(1, rand_limit)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 1:
                raise ValueError
        except ValueError:
            pass
        else:
            if guess == correct_answer:
                print("Just right!")
                break
            elif guess < correct_answer:
                print("Too small!")
            else:
                print("Too large!")


main()

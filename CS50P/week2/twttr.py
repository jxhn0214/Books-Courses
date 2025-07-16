def main():
    # prompt user for tweet
    tweet = input("Input: ")

    # create a list of letters we want to omit
    unacceptable_letters = ['a', 'e', 'i', 'o', 'u']

    print("Output: ", end="")

    # loop through letters and print only acceptable letters
    for letter in tweet:
        if letter.lower() not in unacceptable_letters:
            print(letter, end="")

    print()

main()

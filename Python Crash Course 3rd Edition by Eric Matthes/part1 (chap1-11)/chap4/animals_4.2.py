def main():
    animals = ['dog', 'cat', 'bunny']
    for animal in animals:
        print(animal)
    print("\n")

    print(f"{animals[0].title()}s are omnivores.")
    print(f"{animals[1].title()}s are also omnivores.")
    print(f"{animals[-1].title()}s are herbivores.\n")

    print("all of these animals would make awesome household pets")

main()
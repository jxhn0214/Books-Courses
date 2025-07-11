def main():
    foods = ('burger', 'pizza', 'ramen noodles', 'siopao', 'turon')
    for food in foods:
        print(food)

    foods[0] = 'cereal' # to show you cannot change the contents of a tuple

main()
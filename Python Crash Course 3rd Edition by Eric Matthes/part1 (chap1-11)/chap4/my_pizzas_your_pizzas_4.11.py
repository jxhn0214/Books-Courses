def main():
    my_pizzas = ['pepperoni', 'meat lovers', 'hot mama']
    friend_pizzas = my_pizzas[:]

    my_pizzas.append('deep dish')
    friend_pizzas.append('hawaiian')

    print(f"My favorite pizzas are: {my_pizzas}")
    print(f"My friend's favorite pizzas are: {friend_pizzas}")

main()
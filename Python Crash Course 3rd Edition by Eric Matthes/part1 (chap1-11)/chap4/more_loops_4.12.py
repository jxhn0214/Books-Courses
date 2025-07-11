def main():
    my_foods = ['pizza', 'falafel', 'carrot cake']
    friend_foods = my_foods[:]

    my_foods.append('cannoli')
    friend_foods.append('ice cream')

    print("My favorite two foods are:")
    for food in my_foods[0:2]:
        print(food)

    print("\nMy friend's two favorite foods are:")
    for food in friend_foods[0:2]:
        print(food)

main()
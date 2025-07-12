def main():
    favorite_fruits = ['mango', 'strawberry', 'pineapple', 'coconut',]
    shopping_list = []

    if 'mango' in favorite_fruits:
        print("adding mango to shopping list...")
        shopping_list.append('mango')
        
    if 'pineapple' in favorite_fruits:
        print("adding pineapple to shopping list...")
        shopping_list.append('pineapple')

    if 'apple' in favorite_fruits:
        print("adding apples to shopping list...")
        shopping_list.append('apple')

    print("\nhere is a list of my favorite fruits: ")
    print(f"{favorite_fruits}\n")

    print("here is a list of the things we are going to get at the market: ")
    print(f"{shopping_list}")

main()
def make_sandwhich(*ingredients):
    print("Here are all the ingredients that you want on your sandwhich:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

make_sandwhich('ham', 'american cheese', 'turkey', 'lettuce')

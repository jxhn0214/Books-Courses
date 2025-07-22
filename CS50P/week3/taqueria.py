def order_food(menu):
    current_total = 0
    while True:
        try:
            order = input("Item: ").title()
        except EOFError:
            break
        if order in menu:
            try:
                added_order = menu[order]
                current_total += added_order
                print((f"total: ${current_total:.2f}"))
            except KeyError:
                continue

def main():

    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

    order_food(menu)

main()
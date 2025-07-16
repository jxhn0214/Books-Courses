def main():
    # Tuple for efficiency because we know accepted coins will not change
    accepted_currency = (25, 10, 5)
    amount_due = 50 # Keeps track of amount needed for coke

    while amount_due > 0: # Payment system
        print(f"Amount Due: {amount_due}")
        payment = int(input("Insert Coin: ")) # Ask for payment

        if payment in accepted_currency: # Only accept payment of 25, 10, or 5 cents
            amount_due -= payment # balance left
            
            if amount_due > 0:
                print(f"Amount Due: {amount_due}") # Keeps from displaying negative int

    print(f"Change Owed: {abs(amount_due)}") # change

main()
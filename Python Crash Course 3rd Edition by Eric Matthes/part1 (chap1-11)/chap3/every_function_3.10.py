def main():
    vacation_spots = ['Bali', 'Maldives', 'Fiji', 'Costa Rica', 'Bora Bora']
    print("\tCustomer: 'can you reccomend me some tropical vacation spots?")
    print(f"\tYou: {vacation_spots}")

    
    print("\n\tCustomer: 'can you sort them in alphabetical order?'")
    print(f"\tYou: {sorted(vacation_spots)}")
    print("\tCustomer: 'okay thank you, can you switch it back now?'")
    print(f"\tYou: {vacation_spots}")

    print("\n\tCustomer: 'can you sort them in reverse alphabetical order (Z-A)?")
    print(f"\tYou: {sorted(vacation_spots, reverse=True)}")
    print("\tCustomer: 'okay thank you, can you revert it back?'")
    print(f"\tYou: {vacation_spots}")

    print("\n\tCustomer: 'can you put them in reverse order?")
    vacation_spots.reverse()
    print(f"\tYou: {vacation_spots}")
    print("\tCustomer: 'okay thank you can you put it back to the originial list?")
    vacation_spots.reverse()
    print(f"\tYou: {vacation_spots}")

    
main()

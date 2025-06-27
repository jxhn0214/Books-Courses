def main():
    places = ['greece', 'tokyo', 'okinawa', 'bora bora', 'bahamas']
    print(f"Original list: {places}\n")

    print(f"Temp alphabetical list: {sorted(places)} ")
    print(f"Original list: {places}\n")

    print(f"Temp reverse-alphabetical list: {sorted(places, reverse=True)} ")
    print(f"Original list: {places}\n")

    places.reverse()
    print(f"Perm reversed list: {places}")
    places.reverse()
    print(f"Originial list: {places}\n")

    places.sort()
    print(f"Perm alphabetical list: {places}")
    places.sort(reverse=True)
    print(f"Perm reverse-alphabetical list: {places}")

main()





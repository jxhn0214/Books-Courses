def city_formatted(city, country):
    city_country = f"{city}, {country}"
    return city_country.title()

while True:
    print("\nEnter a city and then the country in which it is located")
    print("press the letter, 'q' at any time to quit the program\n")

    city = input("City: ")
    if city == 'q':
        break
    country = input("Country: ")
    if city == 'q':
        break

    print(f"\n{city_formatted(city, country)}")
def main():
    rivers = {
        'mississippi': 'united states',
        'rio grande': 'mexico',
        'nile': 'egypt'
    }

    for river, country in rivers.items():
        print(f"The {river.title()} river runs through {country.title()}")

    print("\nHere is a list of the rivers:")
    for river in rivers.keys():
        print(river.title())

    print("\nHere is a list of the countries:")
    for country in rivers.values():
        print(country.title())

main()
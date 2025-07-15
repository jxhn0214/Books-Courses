def main(): 
    cities = {
        'san francisco': {
            'country': 'united states',
            'population': '809K',
            'fact': 'has the largest and oldest china town'
        },

        'tokyo': {
            'country': 'japan',
            'population': '37M',
            'fact': 'once called Edo'
        },

        'paris': {
            'country': 'france', 
            'population': '10M',
            'fact': 'nicknamed city of light'
        }
    }

    print("Here is some information about three cities: \n")
    for city, city_info in cities.items():
        print(f"{city}:")
        print(f"\tCountry: {city_info['country']}")
        print(f"\tPopulation: ~{city_info['population']}")
        print(f"\tFun Fact: {city_info['fact']}")

main()
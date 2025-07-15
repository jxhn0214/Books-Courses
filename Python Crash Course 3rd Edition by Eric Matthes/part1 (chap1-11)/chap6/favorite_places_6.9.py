def main():
    favorite_places = {
        'angelyn': ['field', 'mcdonalds', 'with s/o'],
        'giya': ['mall', 'boba shop', 'restaurant'],
        'gerald': ['nike store', 'north face', 'game stop']
    }

    for name, place in favorite_places.items():
        print(f"Here is a list of {name.title()}'s favorite places to go"
              f"{place}")
        
main()
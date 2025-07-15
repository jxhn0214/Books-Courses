def main():
    pet_0 = {
        'angge': 'pomeranian'
    }

    pet_1 = {
        'beth': 'manecoon'
    }

    pet_2 = {
        'giya': 'maz'
    }

    pets = [pet_0, pet_1, pet_2]
    for pet in pets:
        for owner, breed in pet.items():
            print(f"{owner.title()} has a {breed.title()}")

main()
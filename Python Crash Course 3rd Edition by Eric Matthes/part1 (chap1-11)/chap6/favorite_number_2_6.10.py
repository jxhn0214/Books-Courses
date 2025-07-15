def main():
    favorite_numbers = {
        'john': [6, 7, 13],
        'teddy': [9, 28, 2],
        'george': [3, 18, 4],
        'franklin': [9, 34, 22],
        'william': [2, 4, 3],
    }

    for name, nums in favorite_numbers.items():
        print(f"{name.title()}'s favorite numbers are: {nums}")

main()
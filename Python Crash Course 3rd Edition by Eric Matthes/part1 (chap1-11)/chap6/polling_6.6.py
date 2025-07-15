def main():
    favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    'angelyn': '',
    'teddy': '',
    'josh': ''
    }
    
    taken_poll = ['jen', 'sarah', 'edward', 'phil'] 

    for name in favorite_languages.keys():
        if name in taken_poll:
            print(f"{name.title()}, thank you for responding")
        else:
            print(f"{name.title()}, please take the poll.")

main()

    
def main():
    current_users = ['bushcampdad', 'outdoorboy', 'teddyweddy', 'happycamper',
                     'danishdelight']
    new_users = ['TeddyWeddy', 'ilikepizza', 'OutdoorBoy', 'pythonix', 'XnoobX']
    
    for new_user in new_users:
        if new_user.lower() in current_users:
            print(f"Sorry, the username {new_user} has already been taken.")
        else:
            print(f"Hello {new_user}, welcome to the platform.")

main()
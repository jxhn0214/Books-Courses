def main():
    usernames = []

    if usernames: 
        for username in usernames:
            if username == 'admin':
                print(f"hello {username}, would you like to see today's report.")
            else:
                print(f"hello {username}, thank you or signing back in again.")
    else:
        print("We need to find some users!")
        
main()
        
            

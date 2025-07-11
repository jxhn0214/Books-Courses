def main():
    car = "Porsche"
    print(f"is car == porsche? {car.lower() == 'porsche'}\n")

    user_0 = 17
    user_1 = 19 

    if (user_0 >= 18) and (user_1 >= 18):
        print("both users are 18 or older")
    else:
        print("both users are not 18 years old")
    
    if (user_0 >= 18) or (user_1 >= 18):
        print("atleast one user is older than 18\n")

    verified_users = ['john', 'angelyn', 'teddy', 'adam', 'joseph']
    new_user = 'marie'

    if new_user not in verified_users:
        print(f"{new_user.title()} is not a verified user")
    
    if 'john' in verified_users:
        print(f"john is a verified user")

main()
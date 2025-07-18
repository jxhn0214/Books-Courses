class User:
    """Class of user information"""

    def __init__(self, first, last, number, email):
        self.first = first
        self.last = last
        self.number = number
        self.email = email

    def describe_user(self):
        print(f"""
              User Information
              \tFirst name: {self.first}
              \tLast name: {self.last}
              \tPhone number: {self.number}
              \tEmail: {self.email} 
              """)
    
    def greet_user(self):
        print(f"Hello, {self.first.title()} {self.last.title()} welcome to my program")

user0 = User('blake', 'liver', '839-938-394', 'blakeliver@gmail.com')
user1 = User('saegma', 'boin', '993-934-0039', 'sboin@icloud.com')

user0.greet_user()
user0.describe_user()

print()

user1.greet_user()
user1.describe_user()
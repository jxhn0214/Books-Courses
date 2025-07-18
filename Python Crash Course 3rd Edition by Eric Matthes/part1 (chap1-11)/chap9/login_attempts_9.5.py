class User:
    """Class of user information"""

    def __init__(self, first, last, number, email):
        self.first = first
        self.last = last
        self.number = number
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"""
              User Information
              \tFirst name: {self.first}
              \tLast name: {self.last}
              \tPhone number: {self.number}
              \tEmail: {self.email} 
              \tLogin Attempts: {self.login_attempts}""")
    
    def greet_user(self):
        print(f"Hello, {self.first.title()} {self.last.title()} welcome to my program")

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

user0 = User('blake', 'liver', '839-938-394', 'blakeliver@gmail.com')
user1 = User('saegma', 'boin', '993-934-0039', 'sboin@icloud.com')

for _ in range (1, 6):
    user0.increment_login_attempts()

user0.describe_user()

user0.reset_login_attempts()

user0.describe_user()
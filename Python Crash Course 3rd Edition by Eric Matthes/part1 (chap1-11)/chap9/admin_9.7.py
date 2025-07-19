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

class Admin(User):
    """Child class of admin that gives special abilities to admin users"""

    def __init__(self, first, last, number, email):
        """Inherit attributes and initialize a specialized attribute"""
        super().__init__(first, last, number, email)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(self.privileges)


admin = Admin('johny', 'cash', '907-842-8883', 'johnycash@gmail.com')
admin.show_privileges()
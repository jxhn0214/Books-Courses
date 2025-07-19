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


class Privileges:
    """Class that deals with privileges that shows what privileges users have"""

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(self.privileges)
    

class Admin(User):
    """Child class of admin that gives special abilities to admin users"""

    def __init__(self, first, last, number, email):
        """Inherit attributes and initialize a specialized attribute"""
        super().__init__(first, last, number, email)
        self.privileges = Privileges()


admin = Admin('johny', 'cash', '847-883-8839', 'johnycash@gmail.com')
admin.privileges.show_privileges()

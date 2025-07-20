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


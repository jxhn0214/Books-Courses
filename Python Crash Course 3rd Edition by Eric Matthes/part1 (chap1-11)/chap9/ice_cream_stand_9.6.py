class Restaurant:
    """Restaurant class with name and cuisine type as attributes"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"This restaurant is called, {self.restaurant_name.title()}")
        print(f"This restaurant serves {self.cuisine_type.title()} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open and ready for customers")


class IceCreamStand(Restaurant):
    """Attempt to make child class of restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """
        Inherit methods and attributes from parent class 
        and initialize a unique attribute ice_cream_flavors
        """
        super().__init__(restaurant_name, cuisine_type)
        self.ice_cream_flavors = ['vanilla', 'chocolate', 'cookies & cream']

    def show_flavors(self):
        print(f"Here is a list of ice cream flavors that {self.restaurant_name.title()} offers:")
        for ice_cream in self.ice_cream_flavors:
            print(f"\t-{ice_cream.title()}")


ice_cream_stand = IceCreamStand('sweet scoops', 'american')
ice_cream_stand.show_flavors()

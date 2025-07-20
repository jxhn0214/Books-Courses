class Restaurant:
    """Restaurant class with name and cuisine type as attributes"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"This restaurant is called, {self.restaurant_name.title()}")
        print(f"This restaurant serves {self.cuisine_type.title()} cuisine.\n")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open and ready for customers")


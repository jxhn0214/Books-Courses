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

restaurant0 = Restaurant('henry', 'american')
restaurant1 = Restaurant('la lune blanche', 'french')
restaurant2 = Restaurant('saffron orchid', 'indian')

restaurant0.describe_restaurant()
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
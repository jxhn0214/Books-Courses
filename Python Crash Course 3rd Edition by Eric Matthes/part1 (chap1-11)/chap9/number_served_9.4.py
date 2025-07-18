class Restaurant:
    """Restaurant class with name and cuisine type as attributes"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"This restaurant is called, {self.restaurant_name.title()}")
        print(f"This restaurant serves {self.cuisine_type.title()} cuisine.")
        print(f"This restaurant has served {self.number_served} people")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open and ready for customers")

    def set_number_served(self, num_served):
        self.number_served = num_served

    def increment_number_served(self, plus_num_served):
        self.number_served += plus_num_served
    
restaurant = Restaurant("henry", "american")
restaurant.describe_restaurant()
print()

restaurant.set_number_served(50)
restaurant.describe_restaurant()

print("\nOver the next two hours Henry's served 40 more people")
restaurant.increment_number_served(40)
restaurant.describe_restaurant()


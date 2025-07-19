class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
       """Intialize attributes of car""" 
       self.make = make
       self.model = model 
       self.year = year 
       self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """ print statement about car mileage"""
        print(f"This car has {self.odometer_reading} miles on it")
    
    def update_odometer(self, mileage):
        """change mileage with an attribute only if it makes sense"""
         
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back an odometer!")
           
    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size=40):
        """Initialize battery's attribute"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_range(self):
        """Print a statement about the range of this battery"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge")

    def upgrage_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65


class ElectricCar(Car):
    """Represents aspects of a car, specific to an electric one"""

    def __init__(self, make, model, year):
        """Initialize attributes from parent class"""

        super().__init__(make, model, year)
        self.battery = Battery()


leaf = ElectricCar('nissan', 'leaf', 2024)
leaf.battery.get_range()
leaf.battery.upgrage_battery()
leaf.battery.get_range()
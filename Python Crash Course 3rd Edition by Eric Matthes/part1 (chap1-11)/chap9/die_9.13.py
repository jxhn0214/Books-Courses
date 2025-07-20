from random import randint

class Die:
    """Attempt to make a Die that gives us a random number 1-6"""
    
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        self.roll_die = randint(1, self.sides)
        print(f"you rolled a {self.roll_die} on a {self.sides}-sided die")

six_sided_die = Die(6)
six_sided_die.roll_die()

ten_sided_die = Die(10)
ten_sided_die.roll_die()

twenty_sided_die = Die(20)
twenty_sided_die.roll_die()

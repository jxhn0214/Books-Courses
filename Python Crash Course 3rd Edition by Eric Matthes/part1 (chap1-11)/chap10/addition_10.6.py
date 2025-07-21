print("Provide two numbers to sum\n")

try:
    number_0 = int(input("Enter your first number: "))
    number_1 = int(input("Etner your second number: "))
except ValueError:
    print("You did not insert a valid number")
else:
    sum = number_0 + number_1
    print(f"The sum of {number_0} + {number_1} is {sum}.")
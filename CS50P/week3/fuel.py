
def convert_fraction_to_percent(numerator, denominator):
        conversion = (numerator / denominator)
        fuel_percentage = round(conversion * 100)
        return fuel_percentage

def display_fuel_gauge(fuel_percentage):
    if fuel_percentage <= 1:
        print("E")
    elif fuel_percentage >= 99:
        print("F")
    else:
        print(f"{fuel_percentage}%")

def main():
    while True:
        fraction = input("Fraction: ")
        try:
            numerator, denominator = fraction.split("/")
        except ValueError:
             continue

        try:
            numerator = int(numerator)
            denominator = int(denominator)
            if denominator == 0:
                 raise ZeroDivisionError
            elif (denominator < 0) or (numerator < 0):
                 raise ValueError
            elif numerator > denominator:
                continue
        except(ValueError, ZeroDivisionError):
             continue
        else:
            fuel = convert_fraction_to_percent(numerator, denominator)
            display_fuel_gauge(fuel)

        break



main()
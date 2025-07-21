from employee_module import Employee

print("Enter 'q' as your first or last name to exit the program")

while True:
    first = input("Enter your first name: ")
    if first == 'q':
        break

    last = input("Enter your last name: ")
    if last == 'q':
        break

    salary = int(input("Enter your annual salary: "))

    employee0 = Employee(first, last, salary)

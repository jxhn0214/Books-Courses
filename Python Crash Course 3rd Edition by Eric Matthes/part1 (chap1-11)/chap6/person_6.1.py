def main():
    person = {'first_name': 'Lebron',
              'last_name': 'James', 
              'age': 40,
              'city': 'Los Angeles'
              }
    
    name = (f"{person['first_name']} {person['last_name']}")
    print(f"{name} is {person['age']} and lives in the city of {person['city']}.")

main()
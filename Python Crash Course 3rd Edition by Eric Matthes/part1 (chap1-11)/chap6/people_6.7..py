def main():
    person_0 = {
        'first': 'lebron',
        'last': 'james', 
        'location': 'los angeles'
    }

    person_1 = {
        'first': 'terrance',
        'last': 'tao', 
        'location': 'los angeles'

    } 

    person_2 = {
        'fist': 'mark', 
        'last': 'zuckerberg',
        'location': 'palo alto'
    }

    people = [person_0, person_1, person_2]
    for person in people:
        print(f"{person}\n")

main()
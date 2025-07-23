def main():
    grocery_list = [] #unique list for storing grocery names
    grocery_qty = [] #normal list for storing gorcery quantity

    while True:
        try:
            grocery = input()
            grocery_qty.append(grocery) #append every grocery to qty
        except EOFError:
            grocery_list = sorted(set(grocery_qty)) #make unique list to print names

            for grocery in grocery_list:
                print(grocery_qty.count(grocery), grocery.upper())
                #counts all instances of grocery in qty list and prints unique name
            break

main()


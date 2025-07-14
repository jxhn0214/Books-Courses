def main():
    glossary = {
        'list': 'a list of elements', 
        'tuple': 'a non-dynamic list',
        'dictionary': 'a list that holds key-values', 
        'conditional': 'a statement that returns True or False', 
        'for loop': 'a loop composed of intializer, conditon, iterator',
        '.keys()': 'method loops through the keys in a specified dictionary',
        '.values()': 'method loops through the keys in a specified dictionary',
        'set()': 'is a function that creates a set of unique items (without duplicates)',
        'set': 'is essentially a dictionary without key-value pairs',
        '.items()': 'is a method that assigns our keys and values to two indiviudal variables'
    }

    for word, definition in glossary.items(): 
        print(f"A {word} is {definition}")


main()
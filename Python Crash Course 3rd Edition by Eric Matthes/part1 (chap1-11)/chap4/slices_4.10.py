def main():
    ten_cubes = [value ** 3 for value in range (1, 11)]
    print(f"Three first three items in the list are: {ten_cubes[:3]}") #prints the first 3 elements in the list index 0, 1, 2
    print(f"Three items in the middle of the list are {ten_cubes[4:7]}") #prints 3 elements from the middle of the list
    print(f"Three items from the end of the list are: {ten_cubes[-3:]}") #prints 3rd to last element until the end of the list

main()
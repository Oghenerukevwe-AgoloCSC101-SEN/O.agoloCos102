# Swapping ages program
name1 = input("Enter first name: ")
age1 = int(input(f"Enter {name1}'s age: "))

name2 = input("Enter second name: ")
age2 = int(input(f"Enter {name2}'s age: "))

print(f"\nBefore Swap:\n{name1}: {age1}, {name2}: {age2}")

# Swapping the ages
age1, age2 = age2, age1

print(f"\nAfter Swap:\n{name1}: {age1}, {name2}: {age2}")

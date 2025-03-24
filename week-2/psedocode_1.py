# Store checkout system
items = {"Bread": 2.5, "Milk": 1.8, "Eggs": 3.0}
total = sum(items.values())

print(f"Total Amount: ${total:.2f}")
payment = float(input("Enter payment amount: "))

if payment >= total:
    change = payment - total
    print(f"Payment accepted. Change: ${change:.2f}")
else:
    print("Insufficient payment. Please try again.")


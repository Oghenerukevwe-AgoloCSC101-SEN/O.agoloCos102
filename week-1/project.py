def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def compound_interest(principal, rate, time):
    return principal * ((1 + rate / 100) ** time) - principal

def annuity_plan(payment, rate, time):
    rate = rate / 100  # Convert percentage to decimal
    return payment * ((1 + rate) ** time - 1) / rate

# Taking user inputs
P = float(input("Enter Principal Amount: "))
R = float(input("Enter Rate of Interest: "))
T = float(input("Enter Time Period in years: "))

# Calculating and displaying results
print("\nSimple Interest:", simple_interest(P, R, T))
print("Compound Interest:", compound_interest(P, R, T))

# Taking input for annuity
payment = float(input("\nEnter Periodic Payment for Annuity Plan: "))
print("Annuity Plan Amount:", annuity_plan(payment, R, T))

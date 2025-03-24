import cmath

def solve_quadratic(a, b, c):
    """Solves a quadratic equation Ax² + Bx + C = 0."""
    if a == 0:
        return "Not a valid quadratic equation."
    
    d = (b**2) - (4*a*c)  # Discriminant
    root1 = (-b + cmath.sqrt(d)) / (2*a)
    root2 = (-b - cmath.sqrt(d)) / (2*a)
    return root1, root2

def solve_cubic(a, b, c, d):
    """Solves a cubic equation Ax³ + Bx² + Cx + D = 0 using Cardano's method."""
    if a == 0:
        return "Not a valid cubic equation."

    # Convert to depressed cubic form: x³ + px + q = 0
    p = (3*a*c - b**2) / (3*a**2)
    q = (2*b**3 - 9*a*b*c + 27*a**2*d) / (27*a**3)
    
    # Calculate discriminant
    discriminant = (q**2 / 4) + (p**3 / 27)

    if discriminant > 0:
        u = (-q / 2 + cmath.sqrt(discriminant))**(1/3)
        v = (-q / 2 - cmath.sqrt(discriminant))**(1/3)
        root1 = u + v - (b / (3*a))
        return root1, "One real root, two complex roots."
    else:
        theta = cmath.acos(-q / (2 * cmath.sqrt(-p**3 / 27)))
        r = 2 * cmath.sqrt(-p / 3)
        root1 = r * cmath.cos(theta / 3) - (b / (3*a))
        root2 = r * cmath.cos((theta + 2*cmath.pi) / 3) - (b / (3*a))
        root3 = r * cmath.cos((theta - 2*cmath.pi) / 3) - (b / (3*a))
        return root1, root2, root3

def solve_quartic(a, b, c, d, e):
    """Solves a quartic equation Ax⁴ + Bx³ + Cx² + Dx + E = 0 using Ferrari's method."""
    if a == 0:
        return "Not a valid quartic equation."
    
    # Currently, solving quartic equations manually is complex.
    # You can use numerical solvers like scipy.optimize.fsolve or Newton’s method for an exact solution.
    return "Quartic equation solving requires numerical methods."

def main():
    print("Choose the type of equation to solve:")
    print("1. Quadratic (Ax² + Bx + C = 0)")
    print("2. Cubic (Ax³ + Bx² + Cx + D = 0)")
    print("3. Quartic (Ax⁴ + Bx³ + Cx² + Dx + E = 0)")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        a = float(input("Enter coefficient A: "))
        b = float(input("Enter coefficient B: "))
        c = float(input("Enter coefficient C: "))
        print("Roots:", solve_quadratic(a, b, c))

    elif choice == "2":
        a = float(input("Enter coefficient A: "))
        b = float(input("Enter coefficient B: "))
        c = float(input("Enter coefficient C: "))
        d = float(input("Enter coefficient D: "))
        print("Roots:", solve_cubic(a, b, c, d))

    elif choice == "3":
        a = float(input("Enter coefficient A: "))
        b = float(input("Enter coefficient B: "))
        c = float(input("Enter coefficient C: "))
        d = float(input("Enter coefficient D: "))
        e = float(input("Enter coefficient E: "))
        print("Roots:", solve_quartic(a, b, c, d, e))

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

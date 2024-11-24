def solve_linear(a, b, c):
    """Solve ax + by = c for x."""
    if a == 0 and b == 0:
        return "Invalid: Both a and b cannot be zero."
    elif a == 0:
        return f"x: Not Defined, y = {c / b}"
    elif b == 0:
        return f"x = {c / a}, y: Not Defined"
    else:
        return f"x = {c / a}, y = {c / b}"

def solve_quadratic(a, b, c):
    """Solve ax² + bx + c = 0."""
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No Real Roots"
    elif discriminant == 0:
        root = -b / (2*a)
        return f"One Root: x = {root}"
    else:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return f"Two Roots: x1 = {root1}, x2 = {root2}"

def solve_cubic(a, b, c, d):
    """Solve ax³ + bx² + cx + d = 0. For simplicity, approximate a root."""
    if a == 0:
        return "Not a cubic equation."
    from sympy import symbols, solve
    x = symbols('x')
    equation = a*x**3 + b*x**2 + c*x + d
    roots = solve(equation)
    return f"Roots: {roots}"
from sympy import symbols, sqrt, diff, oo
from write import write_to_excel_2

def find_n_for_trapezoid(allowed_error: float, upper_bound: float = 1.1, lower_bound: float = 0):
    """
    ET <= (k * ((b-a)^3)) / 12n^2
    where:

    ET is the error tolerance
    k is the highest value of the second derivative of the function
    b is the upper bound
    a is the lower bound
    n is the number of intervals
    y = sqrt(r^2 - x^2)
    """
    x = symbols('x')

    # Define the constant
    r: float = 1.1

    # Define the function
    y = sqrt(r**2 - x**2)

    # Second derivative
    second_derivative = diff(diff(y, x), x)

    # Evaluate the second derivative at x = 0
    second_derivative_at_x0 = second_derivative.subs(x, 0)
    print("Second derivative at x = 0:", second_derivative_at_x0)
    # Evaluate the second derivative at x = 1.1
    second_derivative_at_1_1 = second_derivative.subs(x, 1.1)
    print("Second derivative at x = 1.1:", second_derivative_at_1_1)
    # Determine the value of k
    if second_derivative_at_1_1.is_finite and second_derivative_at_x0.is_finite:
        k = max(abs(second_derivative_at_1_1), abs(second_derivative_at_x0))
    elif second_derivative_at_x0.is_finite:
        k = second_derivative_at_x0
    elif second_derivative_at_1_1.is_finite:
        k = second_derivative_at_1_1
    else:
        k = oo
    n_for_trapezoid = sqrt((abs(k) * (upper_bound - lower_bound)**3) / (24 * allowed_error))
    print("Number of intervals for the trapezoidal rule:", n_for_trapezoid)
    print("Number of intervals rounded for the trapezoidal rule:", round(n_for_trapezoid))
    data = [
        ("Attribute", "Value"),
        ("rule", "Trapezoid rule"),
        ("allowed error", allowed_error),
        ("k (max of second derivative)", str(abs(k))),
        ("Upper bound", r),
        ("Lower bound", 0),
        ("Number of intervals", str(n_for_trapezoid)),
        ("Number of intervals rounded", str(round(n_for_trapezoid)))
    ]
    write_to_excel_2(data, "errors_calc.xlsx")

def find_n_for_midpoint(allowed_error: float, upper_bound: float = 1.1, lower_bound: float = 0):
    """
    EM <= (k * ((b-a)^3)) / 24n^2
    where:

    ET is the error tolerance
    k is the highest value of the second derivative of the function
    b is the upper bound
    a is the lower bound
    n is the number of intervals
    y = sqrt(r^2 - x^2)
    """
    x = symbols('x')

    # Define the constant
    r = 1.1

    # Define the function
    y = sqrt(r**2 - x**2)

    # Second derivative
    second_derivative = diff(diff(y, x), x)
    # Evaluate the second derivative at x = 0
    second_derivative_at_x0 = second_derivative.subs(x, 0)
    print("Second derivative at x = 0:", second_derivative_at_x0)
    # Evaluate the second derivative at x = 1.1
    second_derivative_at_1_1 = second_derivative.subs(x, 1.1)
    print("Second derivative at x = 1.1:", second_derivative_at_1_1)
    # Determine the value of k
    if second_derivative_at_1_1.is_finite and second_derivative_at_x0.is_finite:
        k = max(abs(second_derivative_at_1_1), abs(second_derivative_at_x0))
    elif second_derivative_at_x0.is_finite:
        k = second_derivative_at_x0
    elif second_derivative_at_1_1.is_finite:
        k = second_derivative_at_1_1
    else:
        k = oo
    n_for_midpoint = sqrt((abs(k) * (upper_bound - lower_bound)**3) / (12 * allowed_error))
    print("Number of intervals for the midpoint rule:", n_for_midpoint)
    print("Number of intervals rounded for the midpoint rule:", round(n_for_midpoint))
    data = [
        ("Attribute", "Value"),
        ("rule", "Midpoint rule"),
        ("allowed error", allowed_error),
        ("k (max of second derivative)", str(abs(k))),
        ("Upper bound", r),
        ("Lower bound", 0),
        ("Number of intervals", str(n_for_midpoint)),
        ("Number of intervals rounded", str(round(n_for_midpoint)))
    ]
    write_to_excel_2(data, "errors_calc.xlsx")



def find_n_for_simpson(allowed_error: float, upper_bound: float = 1.1, lower_bound: float = 0):
    """
    ES <= (k*b-a^5) / (180n^5)
    where:

    ET is the error tolerance
    k is the highest value of the second derivative of the function
    b is the upper bound
    a is the lower bound
    n is the number of intervals
    y = sqrt(r^2 - x^2)
    """
    x = symbols('x')
    # Define the constant
    r = 1.1
    # Define the function
    y = sqrt(r**2 - x**2)
    # Find thr fourth derivative
    first_derivative = diff(y, x)
    second_derivative = diff(first_derivative, x)
    third_derivative = diff(second_derivative, x)
    fourth_derivative = diff(third_derivative, x)
    # Evaluate the second derivative at x = 0
    fourth_derivative_at_0 = fourth_derivative.subs(x, 0)
    # Evaluate the second derivative at x = 1.1
    fourth_derivative_at_1_1 = fourth_derivative.subs(x, 1.1)
    if fourth_derivative_at_1_1.is_finite and fourth_derivative_at_0.is_finite:
        k = max(fourth_derivative_at_1_1, fourth_derivative_at_0)
    elif fourth_derivative_at_0.is_finite:
        k = fourth_derivative_at_0
    elif fourth_derivative_at_1_1.is_finite:
        k = fourth_derivative_at_1_1
    else:
        k = oo

    n_for_simpson = ((abs(k) * (upper_bound - lower_bound)**5) / (180 * allowed_error))**(1/4)
    print("Number of intervals for Simpson's rule:", n_for_simpson)
    print("Number of intervals rounded for Simpson's rule:", round(n_for_simpson))
    data = [
        ("Attribute", "Value"),
        ("rule", "Simpon's rule"),
        ("allowed error", allowed_error),
        ("k (max of fourth interval)", str(abs(k))),
        ("Upper bound", r),
        ("Lower bound", 0),
        ("Number of intervals", str(n_for_simpson)),
        ("Number of intervals rounded", str(round(n_for_simpson)))
    ]
    write_to_excel_2(data, "errors_calc.xlsx")

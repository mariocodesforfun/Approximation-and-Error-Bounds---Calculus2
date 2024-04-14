from math import sqrt, pi
from write import write_to_excel
from typing import List, Tuple


def calculate_circle_properties(n: int, r: float) -> Tuple[float, List[float], List[float], float, float, float, float]:
    """
    Calculates various properties of a circle using the trapezoidal rule.

    Args:
        n (int): Number of intervals for the approximation (higher n = better accuracy).
        r (float): Radius of the circle.

    Returns:
        Tuple[float, List[float], List[float], float, float, float, float]: Tuple containing Exact area, x_values, y_values, weighted sum, area, full approximation, and pi approximation.
    """
    # Exact area of the circle
    exact_area: float = pi * r**2

    # Set upper bound to circle's radius
    upper_bound: float = r
    # Set lower bound to 0 for circle (the origin of the circle is at (0, 0)
    lower_bound: float = 0
    # Calculate the width of each interval aka delta_x
    delta_x: float = (upper_bound - lower_bound) / n
    # Collect all x values
    x_es: list[float] = [lower_bound + i * delta_x for i in range(n + 1)]
    # Calculate the y values for each x value
    ys: list[float] = [sqrt(r**2 - x**2) for x in x_es]
    # Multiply all y values by 2 except the first and last as per the trapezoidal rule
    weights: list[float] = [2 * y for y in ys[1:-1]]
    # Calculate the weighted sum of function values between first and last
    weighted_sum: float = sum(weights)
    # Calculate 1/4 of the area of the circle since we are only using 1/4 of the circle
    area: float = 0.5 * delta_x * (weighted_sum + ys[0] + ys[-1])
    # Multiply by 4 to get the full circle
    full_approximation: float = area * 4  # Multiply by 4 to get the full circle
    # Pi approximation
    pi_approximation: float = full_approximation / r**2

    return exact_area, x_es, ys, weighted_sum, area, full_approximation, pi_approximation


def circle_trapezoid_approx(n: int, r: float):

    """
    Calculate the approximate area of a circle using the trapezoidal rule and save the results to an Excel file.

    Args:
        n (int): Number of intervals for the approximation (higher n = better accuracy).
        r (float): Radius of the circle.
    """
    # Calculate circle properties
    exact_area, x_values, y_values, weighted_sum, area, full_approximation, pi_approximation = calculate_circle_properties(n, r)

    # Data
    data = [
        ("Attribute", "Value"),
        ("Exact area of the circle", exact_area),
        ("Number of intervals", n),
        ("Radius of the circle", r),
        ("Upper bound", r),
        ("Lower bound", 0),
        ("Width of each interval (delta x)", (r-0) / n),
        ("Weights (excluding x0 and xn)", None),  # We will write these separately
        ("Weighted sum", weighted_sum),
        ("Area", area),
        ("Full approximation", full_approximation),
        ("Pi approximation", pi_approximation)
    ]

    # Write to Excel
    write_to_excel(data, x_values, y_values, "data.xlsx")

from math import sqrt, pi
from typing import List, Tuple
from write import write_to_excel

def calculate_circle_simpson_properties(n: int, r: float) -> Tuple[float, List[float], List[float], float, float]:

    """
    Calculates the approximate area of a circle using Simpson's rule.

    Args:
        n (int): Number of intervals for the approximation (higher n = better accuracy).
        r (float): Radius of the circle.

    Returns:
        float: Approximate area of the circle.
    """

    # Exact area of the circle
    exact_area: float = pi * r**2
    # Set upper bound to circle's radius
    upper_bound: float = r
    # Set lower bound to 0 for circle (the origin of the circle is at (0, 0)
    lower_bound: float = 0
    # Calculate the width of each interval (delta_x)
    delta_x: float = (upper_bound - lower_bound) / n
    # Only include n intervals (0 to n+1)
    x_es: list[float] = [lower_bound + i * delta_x for i in range(n+1)]
    # Calculate y values for each x value
    ys: list[float] = [sqrt(r**2 - x**2) for x in x_es]
    # Weight of 1 for the endpoints, 4 for odd-indexed points, and 2 for even-indexed points
    weights: list[float] = [1] + [4 if i % 2 == 1 else 2 for i in range(1, len(ys) - 1)] + [1]
    # Calculate the weighted sum of function values
    weighted_sum: float = sum(weights[i] * ys[i] for i in range(len(ys)))
    # Calculate the approximation using Simpson's rule
    area: float = delta_x / 3 * weighted_sum
    #full_approximation = approximation * 4
    full_approximation: float = area * 4
    # Pi approximation
    pi_approximation: float = full_approximation / r**2

    return exact_area, x_es, ys, weighted_sum, area, full_approximation, pi_approximation

def circle_simpson_approx(n: int, r: float):
    """
    Calculate the approximate area of a circle using Simpson's rule and save the results to an Excel file.

    Args:
        n (int): Number of intervals for the approximation (higher n = better accuracy).
        r (float): Radius of the circle.
    """
    # Calculate circle properties using Simpson's rule
    exact_area, x_values, y_values, weighted_sum, area, full_approximation, pi_approximation = calculate_circle_simpson_properties(n, r)

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

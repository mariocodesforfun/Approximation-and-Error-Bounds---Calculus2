from math import sqrt, pi

from write import write_to_excel
from typing import List, Tuple

def calculate_circle_properties(n: int, r: float) ->  Tuple[float, float, float, float, float]:

    """
    Calculates the approximate area of a circle using the midpoint rule.

    Args:
        n (int): Number of intervals for the approximation (higher n = better accuracy).
        r (float): Radius of the circle.

    Returns:
        Tuple[float, float, float, float, float]: Tuple containing Exact area, weighted sum, area, full approximation, and pi approximation.
    """
    # Exact area of the circle
    exact_area: float = pi * r**2
    # Set upper bound to circle's radius
    upper_bound: float = r
    # Set lower bound to 0 for circle (the origin of the circle is at (0, 0)
    lower_bound: float = 0
    # calculate the width of each interval aka delta_x
    delta_x: float = (upper_bound - lower_bound) / n
    # Only include n intervals (0 to n)
    x_es: list[float] = [lower_bound + (i + 0.5) * delta_x for i in range(n)]
    # Calculate the y values for each x value
    ys: list[float] = [sqrt(r**2 - x**2) for x in x_es]
    #weigthed sum
    weighted_sum: float = sum(ys)
    # Calculate the area of the 1/4 of circle
    area: float = delta_x * weighted_sum
    # Multiply by 4 to get the full circle
    full_approximation: float = area * 4
    # Pi approximation
    pi_approximation: float = full_approximation / r**2

    return exact_area, x_es, ys, weighted_sum, area, full_approximation, pi_approximation


def circle_midpoint_approx(n: int, r: float) -> None:

    """
    Calculate the approximate area of a circle using the midpoint rule and save the results to an Excel file.

    Args:
        n (int): Number of intervals for the approximation (higher n = better accuracy).
        r (float): Radius of the circle.
    """
    exact_area, x_values, y_values, weighted_sum, area, full_approximation, pi_approximation = calculate_circle_properties(n, r)

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

    write_to_excel(data, x_values, y_values, "data.xlsx")

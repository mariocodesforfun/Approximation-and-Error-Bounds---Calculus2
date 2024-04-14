from midpoint_approximation import circle_midpoint_approx
from simpson_approximation  import circle_simpson_approx
from trapezoid_approximation import circle_trapezoid_approx
from calculate_error import (
    find_n_for_midpoint,
    find_n_for_simpson,
    find_n_for_trapezoid
)

# Example usage
circle_trapezoid_approx(12, 1.1)
circle_trapezoid_approx(36, 1.1)
circle_trapezoid_approx(144, 1.1)

circle_midpoint_approx(12, 1.1)
circle_midpoint_approx(36, 1.1)
circle_midpoint_approx(144, 1.1)

circle_simpson_approx(12, 1.1)
circle_simpson_approx(36, 1.1)
circle_simpson_approx(144, 1.1)

find_n_for_trapezoid(0.000001)
find_n_for_midpoint(0.000001)
find_n_for_simpson(0.000001)
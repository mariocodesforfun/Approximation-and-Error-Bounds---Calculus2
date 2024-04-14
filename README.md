# Approximation-and-Error-Bounds---Calculus2

Function-based app that does the following:
1. Calulcates the approximation of the area of a given circle with a given r
2. Calculates the approximation of PI using the found approximation
3. Calulcates how many units are needed for each rule for a given error bound
4. Each time the data is saved in an excel file

All of the three above are done only for the following rules:
1. Trapezoid
2. Midpoint
4. Simpson

#SETUP
1. python3 -m venv '.venv' or python -m venv '.venv'
2. source .venv/bin/activate  or .venv\Scripts\activate
3. pip install -r requirements.txt

Example Usage for finding the approximation of the circle with the following data:
1. n = {12, 36, 144}
2. r = 1.1
3. error_bound = 0.000001

To run the above:
python run.py

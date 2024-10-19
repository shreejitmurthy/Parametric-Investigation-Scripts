# Made because I left my calculator at school

import numpy as np
from scipy.integrate import quad

def get_user_inputs():
    a = float(input("Enter the value for the constant a: "))
    b = float(input("Enter the value for the constant b: "))
    c = float(input("Enter the value for the constant c: "))
    t = float(input("Enter the value for the time t: "))
    return a, b, c, t

def integrand(t, a, b, c):
    return np.sqrt(a**2 + b**2 + (-9.81*t + c)**2)

def compute_arc_length():
    a, b, c, t = get_user_inputs()

    result, error = quad(integrand, 0, t, args=(a, b, c))
    
    # Output the result
    print(f"integral between 0 & {t}: ({a})^2 + ({b})^2 + (-9.81t + {c})^2")
    print(f"Arc length: {round(result, 3)} m")
    print(f"Estimated error: {error}")

compute_arc_length()

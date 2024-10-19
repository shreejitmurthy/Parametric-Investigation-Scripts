# Made because I left my calculator at school

import math

def speed(x, y, z):
    return math.sqrt(x**2 + y**2 + z**2)

x = float(input("x: "))
y = float(input("y: "))
# speed = speed(2.01, -8.34, -9.81)
print(f"√(({x})^2+({y})^2+(-9.81)^2 )")
sp = speed(x, y, -9.81)
print(f"Speed = {round(sp, 3)} ms^-1\n = {round(sp * 3.6, 3)} kmh^-1")
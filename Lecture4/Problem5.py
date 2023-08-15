from math import *

a = int(input())
b = int(input())
c = int(input())

d = b ** 2 - 4 * a * c

if d > 0:
    # 2 real solutions
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print(f"x1 = {x1}, x2 = {x2}")
elif d == 0:
    # 1 real solutions
    x1 = (-b + sqrt(d)) / (2 * a)
    print(f"x1 = {x1}")
else:
    print("No real solutions")

from math import sqrt

a_a = int(input())
b_b = int(input())
c_c = int(input())

pythagoras = sqrt(a_a ** 2 + b_b ** 2)
pythagoras_2 = sqrt(c_c ** 2 + b_b ** 2)
pythagoras_3 = sqrt(a_a ** 2 + c_c ** 2)

print(pythagoras)
print(pythagoras_2)
print(pythagoras_3)

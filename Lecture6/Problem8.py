from math import *

for i in range(1, 8):
    if i == 1:
        for a in range(1, 6):
            if a == 1 or a == 5:
                print(end=" ")
            else:
                print("*", end="  ")
            if a == 5:
                print()

    if i == 1 or i == 2 or i == 5 or i == 6 or i == 7:
        for b in range(1, 6):
            if b == 2 or b == 3 or b == 4:
                print(end="  ")
            else:
                print("*", end=" ")
            if b == 5:
                print()
    if i == 4:
        for a in range(1, 6):
            print("*", end=" ")
            if a == 5:
                print()




count = 0

for i in range(1, 36):
    if 1 <= i <= 4 or 31 <= i <= 34:
        print("*", end=" ")
    elif i == 5 or i == 35:
        print(" ")
    elif 6 <= i <= 30:
        count += 1
        if count % 10 == 1:
            print("*", end="   ")
        if count % 10 == 6:
            print("*", end="   ")
        if count % 10 == 5 or count % 10 == 0:
            print("*")
        if (count % 10 == 2 or
                count % 10 == 3 or
                count % 10 == 4 or
                count % 10 == 7 or
                count % 10 == 8 or
                count % 10 == 9 or
                count % 10 == 10):
            print(" ", end="")


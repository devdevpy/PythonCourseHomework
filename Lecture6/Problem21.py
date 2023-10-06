for i in range(1, 8):
    if i == 1 or i == 2 or i == 5 or i == 6 or i == 7:
        for a in range(1, 6):
            if a == 2 or a == 3 or a == 4:
                print(end="   ")
            else:
                print("* ", end=" ")
            if a == 5:
                print()

    if i == 3:
        for b in range(1, 6):
            if b == 1 or b == 2 or b == 4 or b == 5:
                print("*  ", end="")
            else:
                print(end="   ")
            if b == 5:
                print()

    if i == 4:
        for c in range(1, 6):
            if c == 1 or c == 3 or c == 5:
                print("*", end=" ")
            else:
                print(end="    ")
            if c == 5:
                print()


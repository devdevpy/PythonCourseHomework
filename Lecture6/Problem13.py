for row in range(1, 11):
    for row2 in range(row, row + 10):
        if row2 >= 10:
            print(row2 - 10, end=" ")
            continue
        print(row2, end=" ")
    print()

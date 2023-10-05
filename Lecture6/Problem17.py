n = int(input())

for i in range(1, n + 1):
    if i >= 10:
        i = str(i)
        for j in i:
            print("-", end="")
            print(j, end="")
        continue
    if i != 1:
        print("-", end="")

    print(i, end="")
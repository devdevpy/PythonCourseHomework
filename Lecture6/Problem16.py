num = input()
count = ""

for n in num:
    if n is count:
        continue
    count = n
    print(n, end="")
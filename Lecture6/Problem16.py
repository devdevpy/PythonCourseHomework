num = input()
count = ""

for n in num:
    if n in count:
        continue
    count = n
    print(n, end="")
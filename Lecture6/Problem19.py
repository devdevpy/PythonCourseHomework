text = input().split()

for i in text:
    if len(i) % 2 == 0:
        print(i, end=" ")
    else:
        print(i[::-1], end=" ")

num = int(input())

i = 0
i2 = 0
count = 0
count2 = 0

for i in range(num, num + 9):
    i = str(i)
    rev = i[::-1]
    count += 1
    if i == rev:
        break

for i2 in range(num, num - 9, -1):
    i2 = str(i2)
    rev2 = i2[::-1]
    count2 += 1
    if i2 == rev2:
        break

if count == count2:
    print(i2)
elif count > count2:
    print(i2)
else:
    print(i)
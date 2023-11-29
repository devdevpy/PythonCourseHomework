count2 = 1
count1 = 1
num = 0

list_ = [2, 1, 1, 2, 3, 3, 2, 2, 2, 1]
list_2 = []

for i in range(len(list_) - 1):
    if list_[i] == list_[i + 1]:
        count1 += 1
    else:
        count1 = 1

    if count1 > count2:
        count2 = count1
        num = list_[i]

for a in range(count2):
    list_2.append(num)

print(list_2)

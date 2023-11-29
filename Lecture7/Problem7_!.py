list_ = [3, 2, 3, 4, 2, 2, 4]
list_2 = []
list_3 = []
i = 0

while i < len(list_):
    list_2 = []
    flag = False
    while i < len(list_) - 1 and list_[i] + 1 == list_[i + 1]:
        flag = True
        list_2.append(list_[i])
        i += 1
    if flag:
        list_2.append(list_[i])
    if len(list_3) < len(list_2):
        list_3 = list_2
    i += 1
print(list_3)

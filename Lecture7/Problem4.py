list_ = []
list_1 = []
list_2 = []
list_3 = []

while True:
    words = input()
    if words == "":
        break
    if words < "0":
        list_1.append(words)
    elif words == "0":
        list_2.append(words)
    elif words > "0":
        list_3.append(words)
    list_ = list_1 + list_2 + list_3
for _ in list_:
    print(_)

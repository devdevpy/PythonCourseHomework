list_ = []

while True:
    words = input()
    if words == "":
        break
    if not words in list_:
        list_.append(words)
print(list_)
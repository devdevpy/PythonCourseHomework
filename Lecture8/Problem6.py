dict_ = {
    "yes": "да",
    "no": "не",
    "not": "не"
}
list_ = []
word = input()

for key, value in dict_.items():
    if word == key:
        list_.append(value)
    elif word == value:
        list_.append(key)

print(list_)

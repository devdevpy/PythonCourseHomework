list_ = []

try:
    while True:
        num = int(input())
        if num == 0:
            break
        list_.append(num)
    for i in sorted(list_):
        print(i)
except ValueError:
    print(f"invalid literal for int():")
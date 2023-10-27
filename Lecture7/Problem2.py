list_ = []
count = 0

try:
    while True:
        num = int(input())
        if num <= 0:
            break
        list_.append(num)
        count += 1
    if count < 4 or num < 0:
        print("You must enter a minimum of four positive numbers.")
        exit()
except ValueError:
    print(f"invalid literal for int():")

copy_list = sorted(list_[:])

for i in range(0, 2):
    copy_list.remove(min(copy_list))
    copy_list.remove(max(copy_list))
print(list_, copy_list)

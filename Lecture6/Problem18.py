num = input().lower()
save = ""
count = 0

for n in num:
    if n in save:
        count += 1
    save += n
print(count)

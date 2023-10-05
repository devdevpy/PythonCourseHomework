text = input().split()

for i in text:
    word = i
    i = len(i)
    if i % 2 == 0:
        print(word, end=" ")
    else:
        print(word[::-1], end=" ")

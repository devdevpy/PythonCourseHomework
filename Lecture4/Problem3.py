a = int(input())
b = int(input())
c = int(input())

max_num = 0

if a != b and c != b and a != c:
    if a > b and a > c:
        max_num = a
    elif b > a and b > c:
        max_num = b
    elif c > a and c > b:
        max_num = c

    print(max_num)

elif a == b:
    print(f"a and b contain the same {a} number which is greater than c")

elif b == c:
    print(f"b and c contain the same {b} number which is greater than a")

elif a == c:
    print(f"a and c contain the same {c} number which is greater than b")

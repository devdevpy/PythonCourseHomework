x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())

if ((x1 < x2) and (y1 < y2)) or ((y1 < x2) and (x1 < y2)):
    print("Вмества се")
else:
    print("Не се вмества")

points = int(input())

if 1 <= points <= 3:
    points *= 10
elif 4 <= points <= 6:
    points *= 100
elif 7 <= points <= 9:
    points *= 1000
elif points == 0 or points > 9:
    points = "Error"

print(points)
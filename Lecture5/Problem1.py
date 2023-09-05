num = int(input())

num = str(num)

num1 = num[0:4:3]
num2 = num[1:3]

if num1 < num2:
    print(f"{num2} greater than {num1}")
elif num1 > num2:
    print(f"{num1} greater than {num2}")
elif num1 == num2:
    print(f"{num1} is equal to {num2}")

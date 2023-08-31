num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

if num_1 > num_2:
    if num_1 > num_3:
        if num_2 > num_3:
            print(num_1, num_2, num_3)
        else:
            print(num_1, num_3, num_2)
    else:
        print(num_3, num_1, num_2)
else:
    if num_1 < num_3:
        if num_2 > num_3:
            print(num_2, num_3, num_1)
        else:
            print(num_3, num_2, num_1)
    else:
        if num_2 < num_3:
            print(num_3, num_1, num_2)
        else:
            print(num_2, num_1, num_3)


# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
#
# if (num1 >= num2) and (num1 >= num3) and (num2 >= num3):
#     sort = (num1, num2, num3)
#     print(num1, num2, num3)
# elif (num1 <= num2) and (num1 <= num3) and (num2 <= num3):
#     print(num3, num2, num1)
# elif (num1 >= num2) and (num1 <= num3) and (num2 <= num3):
#     print(num3, num1, num2)
# elif (num1 >= num2) and (num1 <= num3) and (num2 >= num3):
#     print(num2, num1, num3)
# elif (num1 <= num2) and (num1 <= num3) and (num2 >= num3):
#     print(num2, num3, num1)
# elif (num1 <= num2) and (num1 >= num3) and (num2 >= num3):
#     print(num2, num1, num3)
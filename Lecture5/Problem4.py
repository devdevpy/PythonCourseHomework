num = input()

num_1 = num[0]
num_2 = num[1]
num_3 = num[2]

if num_1 == "0" or num_2 == "0" or num_3 == "0":
    print("ZeroDivisionError: division by zero")

else:
    total_sum1 = int(num) / int(num_1)
    total_sum2 = int(num) / int(num_2)
    total_sum3 = int(num) / int(num_3)

    print(num_1, num_2, num_3)
    print(f"{total_sum1:.0f}, {total_sum2:.0f}, {total_sum3:.0f}")

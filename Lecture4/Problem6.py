nums = "{-2, -1, 1}"
nums = nums.strip("{").strip("}")
num_strings = nums.split(",")

first, second, third = int(num_strings[0]), \
                        int(num_strings[1]), \
                        int(num_strings[2])

if first + second + third == 0:
    print(first, second, third)
elif first + second == 0:
    print(first, second)
elif first + third == 0:
    print(first, third)
elif second + third == 0:
    print(second, third)
else:
    print("The sum is not zero")

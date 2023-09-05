a = int(input("Enter a number in the range of[10..99]: "))
b = int(input("Enter a number in the range of[10..99]: "))

total_sum = a * b

if total_sum % 2 == 0:
    total_sum = str(total_sum)
    print(f"{total_sum}, {total_sum[-1]} even")
else:
    total_sum = str(total_sum)
    print(f"{total_sum}, {total_sum[-1]} odd")

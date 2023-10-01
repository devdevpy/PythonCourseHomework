n = 4

sum_ = 0
for num in range(1, n + 1):
    prod = 1
    for num2 in range(num, (2 * num) + 1):
        prod *= num2
    sum_ += prod

print(sum_)

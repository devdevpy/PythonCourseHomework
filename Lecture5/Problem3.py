tank_capacity = int(input())

total_sum = 0
total_sum_2 = 0

integer_sum = tank_capacity // 5
remainder_sum = tank_capacity % 5

if remainder_sum >= 3:
    total_sum = remainder_sum // 3
    total_sum_2 = remainder_sum % 3
    total_sum += integer_sum
    if 0 < remainder_sum < 3:
        remainder_sum += total_sum_2
else:
    if remainder_sum != 0:
        total_sum += integer_sum
        total_sum_2 = remainder_sum % 3


if 0 != total_sum_2 <= 2:
    total_sum_2 = 2
else:
    if remainder_sum < 3:
        total_sum += integer_sum
        remainder_sum += total_sum_2

print(f"{total_sum} times the 2 buckets, an additional {total_sum_2} liter bucket")

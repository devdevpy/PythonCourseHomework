import random

list_nums = []

while True:
    nums = random.randint(1, 50)
    if not nums in list_nums:
        list_nums.append(nums)

        if len(list_nums) == 6:
            list_nums = sorted(list_nums)
            break

print(*list_nums)

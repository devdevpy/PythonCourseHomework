import random

list_nums = []

while True:
    nums = random.triangular(1, 50)
    nums = int(nums)
    if not nums in list_nums:
        list_nums.append(nums)

        if len(list_nums) == 6:
            list_nums = sorted(list_nums)
            break

for i in list_nums:
    print(f"{i}")

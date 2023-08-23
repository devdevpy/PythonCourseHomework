dog_years = int(input())

human_years = 21
total_human_years = 0
total_sum = 0

if dog_years > 2:
    dog_years = dog_years - 2
    total_sum = (dog_years * 4) + human_years

elif dog_years == 2:
    total_sum = human_years

elif dog_years == 1:
    total_sum = (human_years / 2)

print(total_sum)


# dog_years = int(input())
#
# human_years = 0
# total_dog_years = 0
#
# for years in range(dog_years):
#     if years == 0 or years == 1:
#         human_years = 10.5
#         total_dog_years += human_years
#         continue
#     human_years = 4
#     total_dog_years += human_years

# print(total_dog_years)

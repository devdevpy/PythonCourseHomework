dict_ = {}

city = input()

try:

    while city != "":
        lots_of_rain = int(input())

        if city in dict_:
            dict_[city] = lots_of_rain + dict_[city]
        else:
            dict_[city] = lots_of_rain

        city = input()

except ValueError:
    print("invalid literal")

for key, value in dict_.items():
    print("{}: {}".format(key, value))

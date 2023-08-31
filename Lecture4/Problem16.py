month = input()
num_night = int(input())

studio = 0
apartment = 0

if month == "May" or month == "October":
    studio = 50
    apartment = 65

    if num_night > 14:
        apartment *= 0.90
        studio *= 0.70
    elif num_night > 7:
        studio *= 0.95

elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70

    if num_night > 14:
        apartment *= 0.90
        studio *= 0.80

elif month == "July" or month == "August":
    studio = 76
    apartment = 77

    if num_night > 14:
        apartment *= 0.90

price_studio = studio * num_night
price_apartment = apartment * num_night

print(f"Apartment: {price_apartment:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")

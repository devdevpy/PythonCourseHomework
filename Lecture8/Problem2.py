years = 29
gender = "f"
height = 172
kilograms = 63.5
activity_Level = 4
BMR = 0

if activity_Level == 2:
    activity_value = 1.2
elif activity_Level == 3:
    activity_value = 1.375
elif activity_Level == 4:
    activity_value = 1.55
elif activity_Level == 5:
    activity_value = 1.725
elif activity_Level == 6:
    activity_value = 1.9
else:
    activity_value = 1

if gender == "m":
    BMR = 66.47 + (13.75 * kilograms) + (5.003 * height) - (6.755 * years)
elif gender == "f":
    BMR = 655.1 + (9.563 * kilograms) + (1.85 * height) - (4.676 * years)

if activity_value > 0:
    BMR = BMR * activity_value

print(f"Имате нужда от {BMR:.0f} Калории на ден за да поддържате теглото си")
print(f"Имате нужда от {BMR - 500:.0f} Калории на ден за да сваляте по 0.5 кг на седмица")
print(f"Имате нужда от {BMR - 1000:.0f} Калории на ден за да сваляте по 1 кг на седмица")
print(f"Имате нужда от {BMR + 500:.0f} Калории на ден за да качвате по 0.5 кг на седмица")
print(f"Имате нужда от {BMR + 1000:.0f} Калории на ден за да качвате по 1 кг на седмица")

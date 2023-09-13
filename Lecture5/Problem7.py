day = int(input())
month = int(input())
year = int(input())

lear = False

if year % 4 == 0 and year % 100 != 0:

    if year % 400 == 0:
        lear = True
        print(year, "The leap year.")
    else:
        print(year, "Not a leap year.")

elif year % 4 != 0:
    print(year, "Not a leap year.")

elif year % 400 == 0:
    lear = True
    print(year, "The leap year.")

elif year % 400 != 0:
    print(year, "Not a leap year.")

if lear:
    if day == 28 and month == 2:
        print(f"Nex day is: 1, 3, {year}")

    elif (month == 1 or month == 3
            or month == 5 or month == 7
            or month == 8 or month == 10
            or month == 12):

        if day == 31:
            print(f"Nex day is: 1, {month + 1}, {year}")
        else:
            print(f"Nex day is: {day + 1}, {month}, {year}")

    elif (month == 4 or month == 6
          or month == 9 or month == 11):

        if day == 30:
            print(f"Nex day is: 1, {month + 1}, {year}")
        else:
            print(f"Nex day is: {day + 1}, {month}, {year}")
else:
    if (month == 1 or month == 3
          or month == 5 or month == 7
          or month == 8 or month == 10
          or month == 12):

        if day == 31:
            print(f"Nex day is: 1, {month + 1}, {year}")
        else:
            print(f"Nex day is: {day + 1}, {month}, {year}")

    elif (month == 2 or month == 4
          or month == 6 or month == 9
          or month == 11):

        if day == 30 or day == 29:
            print(f"Nex day is: 1, {month + 1}, {year}")
        else:
            print(f"Nex day is: {day + 1}, {month}, {year}")
try:
    age = int(input("Write your years: "))
    gender = input("Write your gender ('M' for Male 'F' for Female): ").upper()
    marital_status = input("marital status ('Y' for Yes 'N' for No): ").upper()

    if gender == "F":
        print("You can only work in urban areas.")
    elif gender == "M":
        if 40 >= age >= 20:
            print("You can work anywhere.")
        elif 60 >= age >= 40:
            print("You can only work in urban areas.")
        else:
            print("Error")
except:
    print("Error")

menu = {"sandwich": 10, "tea": 7, "coffee": 5}

choice = input(f"Please make a selection from the menu: {menu} \n")
total_sum = 0
order = []

while choice != "":
    if choice in menu.keys():
        order.append(menu[choice])
        total_sum = sum(order)
        print(f"Order:{choice} \n{choice} costs {menu[choice]}, total is {total_sum}")
    else:
        print(f"The product you selected is not on the menu: {menu} \n")
    choice = input("Please make a selection from the menu: \n")
print(f"Order total is: {total_sum}")

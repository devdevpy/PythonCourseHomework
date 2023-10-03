from random import choice

list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num = choice(list_)
times = 3
try:
    while not times == 0 :
        user_num = int(input(f"Guess a number in the range 1-9 \n{times} times left : "))
        if user_num > 9 or user_num < 1:
            continue
        times -= 1
        if num > user_num:
            print("Too low")
        elif num < user_num:
            print("Too high")
        else:
            print("Exactly right")
            print("Thank you for playing")
            break
    else:
        print("Sorry, try again!")

except ValueError:
    print("invalid literal")
    print("Sorry, try again!")

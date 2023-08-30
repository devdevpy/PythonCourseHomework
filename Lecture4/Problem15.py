budget = float(input())
category = input()
num_persons = int(input())

transport = 0
ticket = 0

if category == "Normal":
    ticket = 249.99
elif category == "VIP":
    ticket = 499.99

if 1 <= num_persons <= 4:
    transport = budget * 0.75
elif 5 <= num_persons <= 9:
    transport = budget * 0.60
elif 10 <= num_persons <= 24:
    transport = budget * 0.50
elif 25 <= num_persons <= 49:
    transport = budget * 0.40
elif num_persons >= 50:
    transport = budget * 0.25

price_sum = num_persons * ticket + transport
total_sum = abs(budget - price_sum)

if budget > price_sum:
    print(f"Yes! You have {total_sum:.2f} leva left.")
else:
    print(f"Not enough money! You need {total_sum:.2f} leva.")

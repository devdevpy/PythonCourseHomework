temperature = int(input())

status = None

if temperature <= -20:
    status = "icy"

elif 0 >= temperature > -20:
    status = "cold"

elif 15 >= temperature > 0:
    status = "cool"

elif 25 >= temperature > 15:
    status = "warm"

elif temperature > 25:
    status = "hot"

print(status)
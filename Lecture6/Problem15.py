num = int(input("Please enter a number: "))

for p in range(2, num):
    if num % p == 0:
        print(f"The number {num} is not prime.")
        break
else:
    print(f"The number {num} is prime.")

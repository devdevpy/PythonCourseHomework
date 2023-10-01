for a in range(1, 50 + 1):
    for b in range(1, 50 + 1):
        for c in range(1, 50 + 1):
            if a ** 2 + b ** 2 == c ** 3:
                print(f"Found result: {a}^2 + {b}^2 = {c}^3")

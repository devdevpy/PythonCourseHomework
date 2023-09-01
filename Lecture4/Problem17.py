n1 = int(input())
n2 = int(input())
operator = input()

total_sum = 0
even_odd = 0

if operator == "+" or operator == "-" or operator == "*":

    if operator == "+":
        total_sum = n1 + n2

        if total_sum % 2 == 0:
            even_odd = "even"
        else:
            even_odd = "odd"

        print(f"{n1} {operator} {n2} = {total_sum} - {even_odd}")

    elif operator == "-":
        total_sum = n1 - n2

        if total_sum % 2 == 0:
            even_odd = "even"
        else:
            even_odd = "odd"

        print(f"{n1} {operator} {n2} = {total_sum} - {even_odd}")

    elif operator == "*":
        total_sum = n1 * n2

        if total_sum % 2 == 0:
            even_odd = "even"
        else:
            even_odd = "odd"

        print(f"{n1} {operator} {n2} = {total_sum} - {even_odd}")

elif operator == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        total_sum = n1 / n2
        print(f"{n1} {operator} {n2} = {total_sum:.2f}")

elif operator == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        total_sum = n1 % n2
        print(f"{n1} {operator} {n2} = {total_sum}")

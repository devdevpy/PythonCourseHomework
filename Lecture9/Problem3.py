uni = [1, 2, 3, 4, 5, 5, 5, 5]
double = {}
double2 = []

for el in uni:
    if el not in double:
        double[el] = 1
    else:
        double[el] = double[el] + 1

for key, value in double.items():
    if value > 1:
        for k in range(value):
            double2.append(key)

print(double)
print(set(uni))
print(double2)

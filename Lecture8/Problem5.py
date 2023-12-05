d1 = {'a': 1, 'b': 2, 'd': 3}
d2 = {'a': 1, 'b': 2, 'c': 4}
d3 = []
d6 = []
d5 = {}

for value in d2:
    if d1.get(value) != d2.get(value):
        d6.append(d1.get(value))
        d6.append(d2.get(value))
        d5[value] = d6

for value in d1:
    if d1.get(value) != d2.get(value):
        d3.append(d1.get(value))
        d3.append(d2.get(value))
        d5[value] = d3

print(d5)

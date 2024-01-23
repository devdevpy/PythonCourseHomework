l = [5, 4, 3, 1, 7, 16]

# for el in l:
#     if el % 2 == 0:
#         print(el, end=" ")

result = list(map(lambda el: el % 2 == 0, l))
print(result.count(True))
print(result.count(False))

result = list(map(lambda el: el % 2, l))
print(result.count(0))
print(result.count(1))

even = tuple(filter(lambda el: el % 2 == 0, l))
print(len(even))
odd = tuple(filter(lambda el: el % 2 != 0, l))
print(len(odd))

g = sum(map(lambda el: el if el % 2 == 0 else 0, l))
print(result.count(True))
print(result.count(False))

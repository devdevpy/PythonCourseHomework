l = [5, 4, 3, 1, 7, 16]
l2 = [5, 4, 3, 1, 7]

result = list(filter(lambda el: el in l2, l))
print(result)
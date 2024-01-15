from random import *

list_ = [randint(-100, 100) for i in range(5)]
list_positives = []
list_negatives = []

for j in list_:
    if j >= 0:
        list_positives.append(j)
    else:
        list_negatives.append(j)
print(list_)
print(list_positives)
print(list_negatives)

from random import *

list_ = [randint(-100, 100) for i in range(5)]


list_positives = (j for j in list_ if j >= 0)
list_negatives = (j for j in list_ if j < 0)

print(list_)
print(tuple(list_positives))
print(tuple(list_negatives))
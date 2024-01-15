from random import *

list_ = [randint(0, 10) for i in range(10)]
list_2 = [randint(10, 20) for j in range(10)]

result = list_ + list_2
result.sort()
print(result)

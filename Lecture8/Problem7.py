import random
from random import *

dict_ = {1: 1, 1: 2, 1: 3, 1: 4, 1: 5, 1: 6, 2: 1, 2: 2, 2: 3, 2: 4, 2: 5, 2: 6, 3: 1, 3: 2, 3: 3, 3: 4, 3: 5, 3: 6,
         4: 1, 4: 2, 4: 3, 4: 4, 4: 5, 4: 6, 5: 1, 5: 2, 5: 3, 5: 4, 5: 5, 5: 6, 6: 1, 6: 2, 6: 3, 6: 4, 6: 5, 6: 6}
dict_2 = {}

for r in range(1, 1001):
    r_choice = choice(list(dict_.items()))
    print(r_choice)
    dict_2[r_choice[0]] = r_choice[1]

print(dict_2)
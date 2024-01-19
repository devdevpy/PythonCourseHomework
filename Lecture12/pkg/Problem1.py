from random import randint
from typing import List, Any


def found_list(list_: List, element: Any):
    if element in list_:
        print(f"Position: {list_.index(element)}")
    else:
        print("Not found")


element = randint(1, 10)
list_ = [1, 2, 3, 4, 5]
found_list(list_, element)
print(element)

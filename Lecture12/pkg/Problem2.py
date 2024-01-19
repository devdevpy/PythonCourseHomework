from random import randint


def find_list(list_: list, element: int):
    if element in list_:
        return f"Position: {list_.index(element)}"
    else:
        return "Not found"


element = randint(1, 10)
list_ = [1, 2, 3, 4, 5]


def print_found_position():
    print(find_list(list_, element))
    print(f"Random element: {element}")


print_found_position()

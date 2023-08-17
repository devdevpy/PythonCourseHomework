dict_1 = {"1": "Сто", "2": "Двеста", "3": "Триста", "4": "Четиристотин", "5": "Петстотин",
          "6": "Шестстотин", "7": "Седемстотин", "8": "Осемстотин", "9": "Деветстотин"}

dict_2 = {"1": "Десет", "2": "Двадесет", "3": "Тридесет", "4": "Четиридесет", "5": "Петдесет", "6": "Шестдесет",
          "7": "Седемдесет", "8": "Осемдесет", "9": "Деветдесет"}

dict_3 = {"1": "Единадесет", "2": "Дванадесет", "3": "Тринадесет", "4": "Четиринадесет", "5": "Петнадесет",
          "6": "Шестнадесет", "7": "Седемнадесет", "8": "Осемнадесет", "9": "Деветнадесет"}

dict_4 = {"0": "Нула", "1": "Едно", "2": "Две", "3": "Три", "4": "Четири", "5": "Пет",
          "6": "Шест", "7": "Седем", "8": "Осем", "9": "Девет"}

num = int(input("Въведеното число трябва да бъде в следния интервал: 0...999\n"))


nums_symbols = len(str(num))

two_zeros = (str(num).endswith("00"))
one_zero = (str(num).endswith("0"))

index_1 = str(num)[:1]
index_2 = str(num)[1:2]
index_3 = str(num)[2:]

if index_1 == "0":
    dict4 = dict_4.get(index_1)
    print(f"{dict4}")

elif two_zeros:
    dict1 = dict_1.get(index_1)
    print(f"{dict1}")

elif one_zero:
    if nums_symbols == 2:
        dict2 = dict_2.get(index_1)
        print(f"{dict2} ")
    else:
        dict1 = dict_1.get(index_1)
        dict2 = dict_2.get(index_2)
        print(f"{dict1} и {dict2}")

elif index_2 == "0":
    dict1 = dict_1.get(index_1)
    dict4 = dict_4.get(index_3)
    print(f"{dict1} и {dict4}")

elif one_zero:
    dict1 = dict_1.get(index_1)
    dict2 = dict_2.get(index_2)
    print(f"{dict1} и {dict2}")

elif nums_symbols == 3:
    if index_2 == "1":
        dict1 = dict_1.get(index_1)
        dict3 = dict_3.get(index_3)
        print(f"{dict1} и {dict3} ")
    else:
        dict1 = dict_1.get(index_1)
        dict2 = dict_2.get(index_2)
        dict4 = dict_4.get(index_3)
        print(f"{dict1} {dict2} и {dict4} ")

elif nums_symbols == 2:
    if index_1 == "1":
        dict3 = dict_3.get(index_2)
        print(f"{dict3}")
    else:
        dict2 = dict_2.get(index_1)
        dict4 = dict_4.get(index_2)
        print(f"{dict2} и {dict4} ")

elif nums_symbols == 1:
    dict4 = dict_4.get(index_1)
    print(f"{dict4} ")
else:
    print("Въведеното число е невалидно!")

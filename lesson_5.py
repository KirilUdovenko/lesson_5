# словари, методы словарей,
# модули
# функции

# my_dict = {"name": "John", "age": 23, 1: 11}

# print(my_dict, type(my_dict))
# print(my_dict.get("name"))

# person = {"name": "John", "age": 23}
# person_details = {"sex": "Female", "address": "Dnipro", "name": "Jane"}
# new_person = dict()
# new_person.update(person)
# new_person.update(person_details)

# new_person = {**person, **person_details}
# print(new_person)

# person.update(person_details)
# print(person)
# person["sex"] = "Male"
# print(person)


# my_tuple = (("name", "John"), ("age", 23))
# my_list = [("name", "John"), ("age", 23)]
# person = dict(my_tuple)
# print(person)

# address = {"city": "Dnipro", "street": "Polya", "ZIP": 49000}
# skils = {"hard": ["python", "html", "DB", "C++"], "soft": []}
# person = {"name": "John", "age": 23, "skils": skils}
# person_details = {"sex": "Male", "address": address}

# new_person = {**person_details, **person}
# new_person["skils"]["hard"].append("JS")
# print(new_person)

# my_dict = {1: 11, (1,2,3): "test", "1": "TEST"}
# print(11 in my_dict)         # in смотрит только в ключи
#
# # print(my_dict.keys())          # dict_keys почти список
# # keys = list(my_dict.keys)
#
# values = my_dict.values()       # dict_values "почти" список значений
# print(values)

# items = my_dict.items()
# print(items)

# my_dict = {"val_1": 12, "val_2": 24, "val_3": 6, "val_4": 58}
# for key in my_dict:
#     print(key, my_dict[key])
# res_values = []
# res_keys = []
# for value in my_dict.values():
#     if value >10:
#         res_values.append(value)
#
# print(res_values)
# print(res_keys)

# my_temp_dict = {11: 1, 12: 2, 13: 3}
# print(my_temp_dict)
# if len(my_temp_dict.values()) == len(set(my_temp_dict.values())):
#     temp_revers_dict = {value: key for key, value in my_temp_dict.items()}
#     print((temp_revers_dict))

# my_str = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqa"
# res = []
# for symbol in set(my_str):
#     if my_str.count(symbol) == 1:
#         res.append(symbol)
# print(res)
# Использование модулей или пакетов, библиотек
import random # импорт всего модуля
# from random import randint  #Импорт конеретной функции

# value = random.randint(1, 10)
# print(value)
#
# my_list = ["True", "False", "Unknown"]
# my_choice = random.choice(my_list)
# print(my_choice)
#
# random.shuffle(my_list)
# print(my_list)

# from string import ascii_lowercase as alphabet
#
# print(alphabet, type(alphabet))
# random.shuffle(list(alphabet))
# print(alphabet)

import random

# Функции

def create_random_int_number_list(len_list=5):
    numbers = [random.randint(1, 10) for _ in range(len_list)]
    return numbers


def print_dict():       # ВСЁ ЧТО ИСПОЛЬЗУЕМ ТО И ПЕРЕДДАЕМ В ФУНКЦИЮ
    for key, value in person.items():
        print(f"{key}: {value}")

my_dict = {"val_1": 12, "val_2": 24, "val_3": 6, "val_4": 58}
person = {"name": "John", "age": 23, "sex": "Male", "address": {"city": "Dnipro", "street": "Polya", "ZIP": 4900},
          "skils": {"hard": ["python", "html", "DB", "C++"],
                    "soft": []
                    }
          }

# print_dict(person)
# print_dict()
# print_dict(my_dict)
# len_list = random.randint(10, 20)
result = create_random_int_number_list()
print(result)
from time import perf_counter
# from collections import Counter, OrderedDict
from random import randint
from string import ascii_lowercase
import time


def string_generator(number):
    x = time.perf_counter()
    string = ""
    for i in range(number):
        string += ascii_lowercase[randint(1, len(ascii_lowercase)-1)]
    y = time.perf_counter()
    print(y-x)
    print("string generated!")
    return string


def logo(string):
    x = perf_counter()
    logo_dict = {}
    string = string.replace(' ', '')
    # chars_count = dict(OrderedDict(sorted(Counter(string).items())))
    chars_count = {}
    for i in ascii_lowercase:
        chars_count.update({i: string.count(i)})
        # string.replace(i, "")

    keys = list(chars_count.keys())
    values = list(chars_count.values())
    for i in range(3):
        max_value = max(values)
        max_key = keys[values.index(max_value)]
        logo_dict.update({max_key: max_value})
        keys.pop(keys.index(max_key))
        values.pop(values.index(max_value))
    y = perf_counter()
    print(y-x)
    print(logo_dict)


logo(string_generator(10000000))
# logo('google')

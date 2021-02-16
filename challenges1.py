from collections import Counter, OrderedDict


def logo(string):
    logo_dict = {}
    string = string.replace(' ', '')
    chars_count = dict(OrderedDict(sorted(Counter(string).items())))
    keys = list(chars_count.keys())
    values = list(chars_count.values())
    for i in range(3):
        max_value = max(values)
        max_key = keys[values.index(max_value)]
        logo_dict.update({max_key: max_value})
        keys.pop(keys.index(max_key))
        values.pop(values.index(max_value))
    print(logo_dict)


logo('google')

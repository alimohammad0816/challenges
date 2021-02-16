from collections import Counter


def logo(string):
    logo_dict = {}
    string = string.replace(' ', '')
    chars_count = dict(Counter(string))
    keys = list(chars_count.keys())
    values = list(chars_count.values())
    for i in range(3):
        max_value = max(values)
        max_key = keys[values.index(max_value)]
        logo_dict.update({max_key: max_value})
        keys.pop(keys.index(max_key))
        values.pop(values.index(max_value))
    print(logo_dict)


logo('helloworld www this is me and the world l helloworld www this is me ths')

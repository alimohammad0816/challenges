def is_balance(input_string: str) -> bool:
    chars = {
        "{": "}",
        "(": ")",
        "[": "]",
    }

    not_ends = []

    for i in input_string:
        if i in chars.keys():
            not_ends.append(chars[i])

        else:
            if not not_ends or i != not_ends.pop():
                return False

    if not_ends:
        return False

    return True


print(is_balance("[{()}]"))

print(is_balance("}[{}]"))

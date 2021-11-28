def remove_repetitive(input_string: str) -> str:
    # result = sorted("".join(list(set(input_string))))

    result = ""

    for i in input_string:
        if i not in result:
            result += i

    return result


print(remove_repetitive("abbbbbbbbbccccd"))

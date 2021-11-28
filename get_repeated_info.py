def get_repeated_info(numbers: int) -> dict:
    numbers = [i for i in str(numbers)]
    result = {}

    for i in numbers:
        if int(i) not in result:
            result[int(i)] = i * int(i)
        else:
            result[int(i)] += i * int(i)

    return result


print(get_repeated_info(125))

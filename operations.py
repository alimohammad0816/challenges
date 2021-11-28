def operations(input_string: str) -> int:
    input_list = input_string.split(" ")
    result = []

    for i in input_list:
        try:
            result.append(int(i))

        except ValueError:
            if i == "D":
                result.append(result[-1] * 2)

            elif i == "R":
                result.pop()

            elif i == "+":
                result.append(result[-1] + result[-2])

    result = sum(result)

    return result


print(operations("-2 5 D + R"))

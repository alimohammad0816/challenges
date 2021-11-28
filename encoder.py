from string import ascii_lowercase


def encoder(input_string: str, repeat_count: int = 1) -> str:
    letters = ascii_lowercase + ascii_lowercase

    result = f"{input_string[-1]}{input_string[:-1]}"

    for _ in range(repeat_count):
        result = "".join([letters[letters.index(l)+1] for l in result])

    return result


print(encoder("abz", 2))

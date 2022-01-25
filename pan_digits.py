def is_pan_digit(value: str, pan_digit: str) -> bool:
    if len(value) != len(pan_digit):
        return False

    elif not all((str(i) in value for i in pan_digit)):
        return False

    else:
        return True


def find_pandigits():
    p_sum = 0

    for i in range(1, 100):
        for l in range(1, 2000):
            x = f"{i}{l}{i * l}"
            if len(x) == 9:
                if is_pan_digit(x, "123456789"):
                    print(f"{i} * {l} = {i * l}")
                    p_sum += i * l

    return p_sum


find_pandigits()

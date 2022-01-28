def is_pan_digit(value: str, pan_digit: str) -> bool:
    if len(value) != len(pan_digit):
        return False

    elif not all((str(i) in value for i in pan_digit)):
        return False

    else:
        return True


def find_pandigits():
    p_sum = 0
    for i in range(1, 10):
        for l in range(1000, 10000):
            """
            x * yyyy = zzzz to zzzzz
            """
            x = f"{i}{l}{i * l}"
            if len(x) == 9:
                if is_pan_digit(x, "123456789"):
                    print(f"{i} * {l} = {i * l}")
                    p_sum += i * l

    for i in range(10, 100):
        for l in range(100, 1000):
            """
            xx * yyy = zzz to zzzzz
            """
            x = f"{i}{l}{i * l}"
            if len(x) == 9:
                if is_pan_digit(x, "123456789"):
                    print(f"{i} * {l} = {i * l}")
                    p_sum += i * l


find_pandigits()

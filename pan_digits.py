def is_pan_digit(value: int, pan_range: range) -> bool:
    value = str(value)

    if len(value) != len(pan_range):
        return False

    elif not all((str(i) in value for i in pan_range)):
        return False

    else:
        return True


def check_pan_digit(first: int, second: int, pan_digit: int) -> bool:
    third = first * second
    return is_pan_digit(int(f"{first}{second}{third}"), range(1, pan_digit+1))


print(check_pan_digit(12, 2, 2))

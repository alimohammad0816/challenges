from functools import wraps
import re
from typing import Union
from random import choice
import string


email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
phone_regex = r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"


def checker(regex_string: str, items: Union[list, tuple]) -> dict:
    checked_data = {
        "valid": [],
        "invalid": [],
        }

    for item in items:
        if re.match(regex_string, item):
            checked_data["valid"].append(item)
            print("valid")
        else:
            print("invalid")
            checked_data["invalid"].append(item)

    return checked_data


def data_validator(regex_string: str):
    """
    This decorator takes a regex string, and validates the output of the function based on it.
    Will return a dict of validated data, valids and invalids.

    Params
    ------
    regex_string: str
        example: r'some regex'
    
    Returns
    -------
    Dict
    """
    def func_taker(func):
        @wraps(func)
        def args_taker(*args, **kwargs):

            value = func(*args, **kwargs)

            if isinstance(value, str):
                return checker(regex_string, [value])
            
            elif isinstance(value, list):
                return checker(regex_string, value)

            else:
                raise ValueError("values must be string, list or tuple")

        return args_taker    
    return func_taker


@data_validator(email_regex)
def fake_mail_generator(count: int) -> list:
    domains = ["gmail", "yahoo", "hotmail", "outlook"]

    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits

    created_emails = []
    for _ in range(count):
        email = "".join(choice(chars) for _ in range(len(chars))) + "@" + choice(domains) + ".com"
        created_emails.append(email)

    return created_emails


# will return {"valid": ["example@example.com", "example2@example2.com"], "invalid": []}
x = fake_mail_generator(2)

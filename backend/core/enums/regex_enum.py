from enum import Enum


class Regex(Enum):
    BRAND = (
        r'^[a-zA-Z]{2,20}$',
        'Only alphanumeric 2-20 characters allowed.'
    )

    def __init__(self, pattern: str, msg: str):
        self.pattern = pattern
        self.msg = msg

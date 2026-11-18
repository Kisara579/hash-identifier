import re

def is_hexadecimal(value: str) -> bool:
    pattern = r"^[a-fA-F0-9]+$"
    return re.fullmatch(pattern, value) is not None



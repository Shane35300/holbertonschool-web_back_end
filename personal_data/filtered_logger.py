#!/usr/bin/env python3
"""
function called filter_datum that returns the log message obfuscated
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    The function should use a regex to replace occurrences of certain field
    values
    """
    pattern = '|'.join(f'{field}=[^ {separator}]+' for field in fields)
    return re.sub(pattern, lambda m: f'{m.group(0).split("=")[0]}={redaction}',
                  message)

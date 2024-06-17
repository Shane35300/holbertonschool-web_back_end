#!/usr/bin/env python3
"""
function called filter_datum that returns the log message obfuscated
"""
import re
from typing import List
import logging


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    The function should use a regex to replace occurrences of certain field
    values
    """
    pattern = '|'.join(f'{field}=[^ {separator}]+' for field in fields)
    return re.sub(pattern, lambda m: f'{m.group(0).split("=")[0]}={redaction}',
                  message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        """ make a constructor, it updates the class to accept a list of
        strings fields constructor argument"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ filter values in incoming log records using filter_datum. Values
        for fields in fields should be filtered"""
        original_message = super(RedactingFormatter, self).format(record)
        obfuscated_message = filter_datum(self.fields, self.REDACTION,
                                          original_message, self.SEPARATOR)
        return obfuscated_message

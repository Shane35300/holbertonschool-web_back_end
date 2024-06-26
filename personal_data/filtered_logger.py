#!/usr/bin/env python3
"""
function called filter_datum that returns the log message obfuscated
"""
import re
from typing import List, Tuple
import logging
import mysql.connector
import os


# Define PII_FIELDS as a tuple of strings
PII_FIELDS: Tuple[str, ...] = ("name", "email", "phone", "ssn", "password")


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

    def __init__(self, fields: List[str]):
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


def get_logger() -> logging.Logger:
    """
    Create and configure a logger named 'user_data' that logs up to INFO level.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Create StreamHandler with RedactingFormatter
    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=list(PII_FIELDS))
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Return a MySQL database connection object using credentials
    from environment variables.
    """
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')

    return mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=db_name
    )


def main() -> None:
    """Main function to fetch and display user data."""
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users;")

    logger = get_logger()
    for row in cursor:
        message = '; '.join([f"{key}={value}" for key, value in row.items()])
        logger.info(message)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()

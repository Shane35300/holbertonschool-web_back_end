import redis
import uuid
from typing import Union

class Cache:
    def __init__(self):
        """Initializes the Cache instance and flushes the Redis database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the data in Redis using a random key.

        Args:
            data: Data to store in Redis. It can be a string, bytes, int or float.

        Returns:
            str: The key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

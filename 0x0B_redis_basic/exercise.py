import redis
import uuid
from typing import Union, Optional, Callable


class Cache:
    def __init__(self):
        """Initializes the Cache instance and flushes the Redis database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the data in Redis using a random key.

        Args:
            data: Data to store in Redis. It can be a string, bytes,
            int or float.

        Returns:
            str: The key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[[bytes], any]] = None) -> Optional[any]:
        """
        Retrieve data from Redis and apply the optional conversion function.

        Args:
            key (str): The key to retrieve data for.
            fn (Optional[Callable[[bytes], any]]): The function to convert the data.

        Returns:
            Optional[any]: The retrieved and converted data, or None if key does not exist.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve data as a UTF-8 string from Redis.

        Args:
            key (str): The key to retrieve data for.

        Returns:
            Optional[str]: The retrieved string data, or None if key does not exist.
        """
        return self.get(key, fn=lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve data as an integer from Redis.

        Args:
            key (str): The key to retrieve data for.

        Returns:
            Optional[int]: The retrieved integer data, or None if key does not exist.
        """
        return self.get(key, fn=int)

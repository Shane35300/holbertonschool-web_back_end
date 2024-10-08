import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count the number of times a method is called.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The decorated method with call counting functionality.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function to increment the count of method calls in Redis.

        Args:
            self: The instance of the class.
            *args: Positional arguments for the method.
            **kwargs: Keyword arguments for the method.

        Returns:
            The result of the original method call.
        """
        key = method.__qualname__
        # Increment the call count in Redis
        self._redis.incr(key)
        # Call the original method and return its result
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of function calls in Redis.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The decorated method with call history functionality.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function to store function call history in Redis.

        Args:
            self: The instance of the class.
            *args: Positional arguments for the method.
            **kwargs: Keyword arguments for the method.

        Returns:
            The result of the original method call.
        """
        # Generate Redis keys for inputs and outputs
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"

        # Store the input arguments in Redis
        self._redis.rpush(inputs_key, str(args))

        # Call the original method
        result = method(self, *args, **kwargs)

        # Store the output in Redis
        self._redis.rpush(outputs_key, result)

        return result

    return wrapper


class Cache:
    def __init__(self):
        """Initializes the Cache instance and flushes the Redis database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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

    def get(self, key: str,
            fn: Optional[Callable[[bytes], any]] = None) -> Optional[any]:
        """
        Retrieve data from Redis and apply the optional conversion function.

        Args:
            key (str): The key to retrieve data for.
            fn (Optional[Callable[[bytes], any]]): The function to convert the
            data.

        Returns:
            Optional[any]: The retrieved and converted data, or None if key
            does not exist.
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
            Optional[str]: The retrieved string data, or None if key does
            not exist.
        """
        return self.get(key, fn=lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve data as an integer from Redis.

        Args:
            key (str): The key to retrieve data for.

        Returns:
            Optional[int]: The retrieved integer data, or None if key does
            not exist.
        """
        return self.get(key, fn=int)


def replay(method: Callable) -> None:
    """
    Display the history of calls for a particular function.

    Args:
        method (Callable): The method whose call history is to be replayed.
    """
    # Generate Redis keys for inputs and outputs
    inputs_key = f"{method.__qualname__}:inputs"
    outputs_key = f"{method.__qualname__}:outputs"

    # Fetch inputs and outputs from Redis
    inputs = method.__self__._redis.lrange(inputs_key, 0, -1)
    outputs = method.__self__._redis.lrange(outputs_key, 0, -1)

    # Print the history of calls
    print(f"{method.__qualname__} was called {len(inputs)} times:")
    for input_bytes, output_bytes in zip(inputs, outputs):
        input_str = input_bytes.decode("utf-8")
        output_str = output_bytes.decode("utf-8")
        print(f"{method.__qualname__}(*{input_str}) -> {output_str}")

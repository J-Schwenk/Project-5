# Library of General Utility Functions

import time
from functools import wraps


def chunk_list(data: list, chunk_size: int) -> list[list]:
    """
    Splits a list into smaller lists (chunks) of a specified size.

    Args:
        data (list): The list to be split into chunks.
        chunk_size (int): The desired size of each chunk.

    Returns:
        list[list]: A list of chunks, where each chunk is a list.

    Raises:
        ValueError: If `chunk_size` is less than 1.
        TypeError: If `data` is not a list or `chunk_size` is not an integer.

    Example:
        >>> chunk_list([1, 2, 3, 4, 5], 2)
        [[1, 2], [3, 4], [5]]
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list")
    if not isinstance(chunk_size, int):
        raise TypeError("chunk_size must be an integer")
    if chunk_size < 1:
        raise ValueError("chunk_size must be greater than 0")

    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]


def flatten_nested(nested_list: list) -> list:
    """
    Flattens a nested list into a single-level list.

    Args:
        nested_list (list): A list that may contain other lists.

    Returns:
        list: A flat list containing all elements from the input.

    Raises:
        TypeError: If `nested_list` is not a list.

    Example:
        >>> flatten_nested([1, [2, [3, 4]], 5])
        [1, 2, 3, 4, 5]
    """
    if not isinstance(nested_list, list):
        raise TypeError("nested_list must be a list")

    flat_list = []

    def _flatten(sublist):
        for item in sublist:
            if isinstance(item, list):
                _flatten(item)
            else:
                flat_list.append(item)

    _flatten(nested_list)
    return flat_list


def timeit_decorator(func):
    """
    A decorator that measures and prints the execution time of a function.

    Args:
        func (callable): The function to measure.

    Returns:
        callable: The wrapped function with execution time measurement.

    Raises:
        TypeError: If `func` is not callable.

    Example:
        >>> @timeit_decorator
        ... def slow_function():
        ...     time.sleep(2)
        ... slow_function()
        Function 'slow_function' executed in 2.00 seconds
    """
    if not callable(func):
        raise TypeError("func must be callable")

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.2f} seconds")
        return result

    return wrapper
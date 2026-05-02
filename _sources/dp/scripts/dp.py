import sys

from time import time
from typing import List, Any


def memoize(f, limit=1000):
    cache = {}

    def memoized_f(*args):
        key = tuple(args)

        if key not in cache:
            cache[key] = f(*args)
        return cache[key]

    return memoized_f


def timeit(f, *args, **kwargs):
    unit = kwargs.pop("unit", "ms")

    t0 = time()
    result = f(*args, **kwargs)
    t1 = time()
    duration = t1 - t0

    if unit == "ms":
        duration *= 1000

    return result, duration


class ArrayLRUCache:
    def __init__(self, maxsize: int = None) -> None:
        self.maxsize: int = maxsize
        self.cache: List[Any] = [None] * maxsize

    def __getitem__(self, key: int) -> Any:
        return self.cache[key % self.maxsize]

    def __setitem__(self, key: int, value: Any) -> None:
        self.cache[key % self.maxsize] = value

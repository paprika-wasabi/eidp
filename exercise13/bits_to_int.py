from functools import reduce
from typing import Callable

bits_to_int: Callable[[list], int] = lambda bits: reduce(lambda x, y: x * 2 + y, bits)
# def bits_to_int(bits: list) -> int:
#     return reduce(lambda x, y: x*2 + y, bits)
if __name__ == "__main__":
    print(bits_to_int([1, 0, 1, 1, 1, 1]))
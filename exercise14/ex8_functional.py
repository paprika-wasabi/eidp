from   dataclasses import dataclass
from   typing      import Any, Optional, Union
# import math
# import pytest

## Aufgabe 8 (Functional Programming) ##########################################
def twice(f):
    return lambda x: 2 * f(x)


def pythagorean_triples(n):
    for z in range(n):
        for y in range(z):
            for x in range(y):
                if z == ((x ** 2) + (y ** 2)) ** 0.5:
                    yield (x, y, z)


if __name__ == "__main__":
    print(list(pythagorean_triples(15)))
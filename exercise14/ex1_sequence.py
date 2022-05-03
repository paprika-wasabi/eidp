from   dataclasses import dataclass
from   typing      import Any, Optional, Union
import math
# import pytest

## Aufgabe 1 (Sequence) ########################################################

def count_iterations(n):
    count = 0
    while n > 0:
        if n % 3 == 0:
            n = n + 4
            count += 1
        elif n % 4 == 0:
            n = n * 0.5
            count += 1
        else:
            n = n - 1
            count += 1
    return count


if __name__ == "__main__":
    print(count_iterations(5))
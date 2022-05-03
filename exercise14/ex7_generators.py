from   dataclasses import dataclass
from   typing      import Any, Optional, Union
# import math
# import pytest

## Aufgabe 7 (Generators) ######################################################


def my_enumerate(xs):
    result = []
    for i in range(len(xs)):
        result.append((i, xs[i]))
    return result


def prefixes(xs):
    result = []
    for i in range(len(xs) + 1):
        n = list(xs[j] for j in range(i))
        result.append(n)
    return result


def alternate(xs, ys):
    result = []
    s_done = False
    node_done = False
    while True:
        if s_done is True and node_done is True:
            break
        if s_done is False:
            try:
                new_s = next(xs)
                result.append(new_s)
            except StopIteration:
                s_done = True
        if node_done is False:
            try:
                new_node = next(ys)
                result.append(new_node)
            except StopIteration:
                node_done = True
    return result    


if __name__ == "__main__":
    print(list(alternate(iter("abcdefghijklmnopqrstuvxyz"), iter([0, 1, 2,20,31,39,100,234]))))
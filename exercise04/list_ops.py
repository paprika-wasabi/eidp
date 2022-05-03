from math import isclose


def average(x: float) -> float:
    m = sum(x)
    n = len(x)
    if n == 0:
        n = n + 1
    result = m / n
    return result


def reverse(x: int) -> int:
    i = len(x) - 1
    n = 0
    while i >= 0:
        x[n] = i + 1
        n = n + 1
        i = i - 1
    return x


def only_positive(x: int) -> int:
    i = 0
    n = 0
    new_x = []
    while i < len(x):
        if x[n] > 0:
            new_x.append(x[n])
        i = i + 1
        n = n + 1
    return new_x


if __name__ == "__main__":
    eps = 1e-4
    assert isclose(average([]), 0.0, abs_tol=eps, rel_tol=eps)
    assert isclose(average([1.0]), 1.0, rel_tol=eps)
    assert isclose(average([5.0, 10.0, 15.0, 20.0]), 12.5, rel_tol=eps)
    assert reverse([]) == []
    assert reverse([1, 2, 3]) == [3, 2, 1]
    assert reverse([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert only_positive([]) == []
    assert only_positive([1, 2, 3]) == [1, 2, 3]
    assert only_positive([-8, 1, -5, -9, 2, -7, 3, -6, 0]) == [1, 2, 3]
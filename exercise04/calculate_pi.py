from math import sqrt, isclose


def calculate_pi(n: int) -> int:
    if n < 0:
        n = 0
    x = []
    i = 1
    while i <= n:
        a = 1 / pow(i, 2)
        x.append(a)
        i = i + 1
    y = sum(x)
    y = sqrt(y * 6)
    return y


if __name__ == "__main__":
    eps = 1e-4
    assert isclose(calculate_pi(-3), 0.0, abs_tol=eps, rel_tol=eps)
    assert isclose(calculate_pi(1), 2.44948, rel_tol=eps)
    assert isclose(calculate_pi(7), 3.01177, rel_tol=eps)
    assert isclose(calculate_pi(1000), 3.14063, rel_tol=eps)
    assert isclose(calculate_pi(10000), 3.14149, rel_tol=eps)
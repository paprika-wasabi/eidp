def compose(f,g):
    return lambda x: f(g(x))

f = lambda x: x + 1

g = lambda x: x *2

print(compose(f,g)(5))


def factor_pairs(n: int):
    result = []
    result.append((1, n))
    for i in range(n):
        for j in range(n):
            if i * j == n:
                result.append((i, j))
    result.append((n, 1))
    return result


print(factor_pairs(6))
def compose(f, g) -> int:
    return lambda x: f(g(x))


if __name__ == "__main__":
    inc = lambda x: x + 1
    mul2 = lambda x: x * 2
    print(type(inc(mul2(4))))
compose = lambda f, g: lambda x: f(g(x))


def test_compose():
    inc  = lambda x: x + 1
    mul2 = lambda x: x * 2
    assert compose(inc, mul2)(4) == 9

from functools import reduce


bits_to_int = lambda bits: reduce(lambda n, b: n * 2 + b, bits)


def test_bits_to_int():
    assert bits_to_int([1, 0, 1, 0]) == 10

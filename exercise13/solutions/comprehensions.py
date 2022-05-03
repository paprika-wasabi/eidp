normalize_word = lambda s: "".join(c.lower() for c in s if c.isalpha())

is_sorted = lambda xs: all(xs[i] <= xs[j] for i in range(len(xs))
                                          for j in range(len(xs))
                                          if i <= j)


# or a slightly faster alternative:

is_sorted = lambda xs: all(xs[i] <= xs[j] for i in range(0, len(xs))
                                          for j in range(i, len(xs)))


def test_normalize_word():
    assert normalize_word("Ver-BieTen?") == "verbieten"


def test_is_sorted_yes():
    assert is_sorted([1, 3, 4, 5])


def test_is_sorted_no():
    assert not is_sorted([1, 4, 3, 5])


def test_is_sorted_empty():
    assert is_sorted([])

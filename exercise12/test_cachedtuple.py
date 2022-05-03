from cachedtuple import CachedTuple


def test_cachedtuple():
    # create finite cached tuple
    ct = CachedTuple(range(1, 20))
    # assert __getitem__ works and cache grows properly
    assert ct[0] == 1
    assert len(ct.cache) == 1
    assert ct[10] == 11
    assert len(ct.cache) == 11
    assert ct[5] == 6
    assert len(ct.cache) == 11

    # assert IndexError is raised correctly
    try:
        print(ct[25])
        raise RuntimeError("No exception was raised")
    except IndexError:
        pass
    try:
        print(ct[-7])
        raise RuntimeError("No exception was raised")
    except IndexError:
        pass
    assert len(ct) == 19

    # assert that usage is possible as iterator multiple times
    ct_new = CachedTuple(range(1, 20))
    assert list(ct_new) == list(range(1, 20))
    assert list(ct_new) == list(range(1, 20))

    # test infinite generator
    def zero_generator():
        while True:
            yield 0

    ct0 = CachedTuple(zero_generator())
    assert ct0[0] == 0
    assert ct0[1337] == 0
    assert len(ct0.cache) == 1338
    # len(ct0) would run forever

    # test n_max argument
    ct1 = CachedTuple(zero_generator(), n_max=100)
    assert ct1[0] == 0
    assert ct1[57] == 0
    assert len(ct1) == 100, len(ct1)
    assert list(ct1) == [0] * 100
    try:
        print(ct1[125])
        raise RuntimeError("No exception was raised")
    except IndexError:
        pass
    print("Test successful.")


if __name__ == "__main__":
    test_cachedtuple()
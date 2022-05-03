from dataclasses import dataclass


@dataclass
class V3:
    x: int
    y: int
    z: int


mapV3 = lambda f: lambda v, w: V3(f(v.x, w.x), f(v.y, w.y), f(v.z, w.z))


cadd = mapV3(lambda x, y: x + y)
csub = mapV3(lambda x, y: x - y)
cmul = mapV3(lambda x, y: x * y)
cdiv = mapV3(lambda x, y: x // y)
cpow = mapV3(lambda x, y: x ** y)


def test_map2():
    assert mapV3(lambda x, y: x + y)(V3(1, 2, 3), V3(4, 5, 6)) == V3(5, 7, 9)

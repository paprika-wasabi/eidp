from fleet import Bus
import pytest


def test_maut():
    bus = Bus(25, 100000, 2500, 1995, 200, 80, 40)
    assert(bus.maut()) == 3500


def test_assert():
    with pytest.raises(AssertionError):
        Bus(25, 100000, -2500, 1995, 200, 80, 40)

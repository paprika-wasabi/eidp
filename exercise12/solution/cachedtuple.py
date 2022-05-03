from dataclasses import dataclass, field
from typing import Optional, Iterable, Iterator


@dataclass
class CachedTuple:
    iterable: Iterable
    n_max: Optional[int] = None
    iterator: Iterator = field(init=False)
    cache: list = field(init=False)
    finished: bool = field(init=False)

    def __post_init__(self):
        self.iterator = iter(self.iterable)
        self.cache = []
        self.finished = False

    def cache_next(self):
        if not self.finished:
            try:
                self.cache.append(next(self.iterator))
                if self.n_max is not None and len(self.cache) >= self.n_max:
                    self.finished = True
            except StopIteration:
                self.finished = True

    def __getitem__(self, item: int):
        match item:
            case int():
                error_str = "Index " + str(item) + " out of range"
                if item < 0:
                    raise IndexError(error_str)
                while len(self.cache) <= item:
                    self.cache_next()
                    if self.finished:
                        raise IndexError(error_str)
                return self.cache[item]
        raise TypeError("Index must be an integer")

    def __len__(self) -> int:
        while not self.finished:
            self.cache_next()
        return len(self.cache)


def main():
    iterable = range(20)
    cachedtuple = CachedTuple(iterable)
    print(cachedtuple[0])
    print(len(cachedtuple.cache))

    print(cachedtuple[10])
    print(len(cachedtuple.cache))

    print(len(cachedtuple))
    print(len(cachedtuple.cache))

    try:
        print(cachedtuple[25])
    except IndexError as e:
        print(e)

    print(list(cachedtuple))
    print(next(iter(cachedtuple)))
    for x in cachedtuple:
        print(x, end=" ")


if __name__ == "__main__":
    main()

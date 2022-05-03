from dataclasses import dataclass, field
from typing import Iterable, Iterator, Optional


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

    def cache_next(self, item):
        if self.n_max is None:
            for i in range(len(self.cache), item + 1):
                try:
                    mem = next((self.iterator))
                    self.cache.append(mem)
                except StopIteration:
                    self.finished is True
        else:
            if item < self.n_max:
                for i in range(len(self.cache), item + 1):
                    try:
                        mem = next((self.iterator))
                        self.cache.append(mem)
                    except StopIteration:
                        self.finished is True
            else:
                self.finished is True

    def __getitem__(self, item):
        match item:
            case int():
                if item < 0:
                    raise IndexError
                if item == 0:
                    self.cache_next(0)
                    return self.cache[0]
                try:
                    return self.cache[item]
                except IndexError:
                    self.cache_next(item)
                    return self.cache[item]
            case _:
                raise TypeError

    def __len__(self):
        if self.n_max is None:
            count = 0
            for el in self.iterable:
                count = count + 1
            return count
        else:
            return self.n_max
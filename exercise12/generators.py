from typing import Iterator


def collatz(n: int) -> Iterator[int]:
    while True:
        yield n
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int((3 * n) + 1)


def generate_target(generator: Iterator[int], target: int) -> Iterator[int]:
    while True:
        el = next(generator)
        yield el
        if el != target:
            pass
        else:
            break


def arithmetic_mean(generator: Iterator[int]) -> Iterator[int]:
    for el in generator:
        yield el / 2


def map_helper(x: int) -> int:
    return x % 7


def filter_helper(x: int) -> bool:
    if x % 3 == 0 or x % 5 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    input_generator = iter(range(0, 26, 5))
    result = map(map_helper, input_generator)
    print(list(result))
    input_generator = iter(range(20))
    result = filter(filter_helper, input_generator)
    print(list(result))
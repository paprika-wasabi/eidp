from typing import Iterable, Iterator


def collatz(n: int) -> Iterator[int]:
    while True:
        yield n
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1


def generate_target(generator: Iterator, target: int) -> Iterator:
    for x in generator:
        yield x
        if x == target:
            break


def arithmetic_mean(xs: Iterator[float]) -> Iterator[float]:
    i = 0
    total = 0.0
    for x in xs:
        i += 1
        total += x
        yield total / i


def main():
    # collatz
    generator = collatz(11)
    for i in range(20):
        print(next(generator), end=" ")
    print()

    # limited output
    print(list(generate_target(iter(range(10)), 4)))
    print(list(generate_target(collatz(11), 1)))

    # running mean
    print(list(arithmetic_mean(iter(range(0, 21, 4)))))

    # map
    def map_helper(x: int) -> int:
        return x % 7

    input_generator = iter(range(0, 26, 5))
    print(list(map(map_helper, input_generator)))

    # filter
    def filter_helper(x: int) -> bool:
        return x % 3 == 0 or x % 5 == 0

    input_generator = iter(range(20))
    print(list(filter(filter_helper, input_generator)))


if __name__ == "__main__":
    main()

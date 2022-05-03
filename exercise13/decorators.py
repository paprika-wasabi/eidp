import functools


def cached(f):
    cached = {}

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        # begin = time.time()
        if args in cached:
            return cached[args]
        value = f(*args, **kwargs)
        cached[args] = value
        # end = time.time()
        return value
    return wrapper


@cached
def fib_fast_and_simple(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_fast_and_simple(n - 1) + fib_fast_and_simple(n - 2)


if __name__ == "__main__":
    print(fib_fast_and_simple(120))
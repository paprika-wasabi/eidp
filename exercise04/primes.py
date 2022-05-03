def is_prime(n: int) -> int:
    if n > 1:
        for i in range(2, n):
            if(n % i) == 0:
                return 0
        return 1
    else:
        return 0


def primes(x: int) -> int:
    prime_list = []
    j = 1
    while j <= x:
        if is_prime(j) == 1:
            prime_list.append(j)
            j = j + 1
        else:
            j = j + 1
    return prime_list


if __name__ == "__main__":
    assert primes(1) == []
    assert primes(3) == [2, 3]
    assert primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]

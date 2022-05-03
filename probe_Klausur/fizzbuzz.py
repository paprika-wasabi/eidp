def fizzbuzz(n: int) -> str:
    if n % 3 == 0 and n % 5 == 0:
        return "fizzbuzz"
    elif n % 3 == 0 and not n % 5 == 0:
        return "fizz"
    elif n % 5 == 0 and not n % 3 == 0:
        return "buzz"


def test_fizzbuzz():
    assert fizzbuzz(15) == "fizzbuzz"
    assert fizzbuzz(9) == "fizz"
    assert fizzbuzz(10) == "buzz"

print(fizzbuzz(15))
print(fizzbuzz(9))
print(fizzbuzz(10))
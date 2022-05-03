def normalize_word(s: str) -> str:
    result = ''
    return result.join(el.lower() for el in list(filter(lambda el: el.isalpha(), (el for el in s))))


def is_sorted(xs: list) -> bool:
    return all((True if xs[i] <= xs[i + 1] else False) for i in range(len(xs)) if i < len(xs) - 1)


if __name__ == "__main__":
    print(normalize_word("Ver-BieTen?"))
    print(is_sorted([1, 1, 3]))
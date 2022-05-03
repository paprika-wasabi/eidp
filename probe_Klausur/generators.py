from functools import cache


def accumulate(xs):
    cached = []
    for el in xs:
        cached.append(el)
        x = 0
        for item in cached:
            x = x + item
        yield x


def char_range(s: str, e: str) -> list[str]:
    alphabet =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(alphabet)):
        if s == alphabet[i]:
            yield alphabet[i]
            for j in range(i + 1, len(alphabet)):
                if e == alphabet[j]:
                    break
                else:
                    yield alphabet[j]
            yield e
            

def partitions(xs):
    for el in xs:
        part = []
        for xl in xs:
            if el == xl:
                continue
            else:
                part.append(xl)
        yield (el, part)



print(list(accumulate([1,2,3,4])))
print(list(char_range('a','c')))
print(list(partitions([1,2,3,4])))
def to_snake(s: str):
    result = ''
    for el in s:
        if el.isupper():
            result += '_' + str(el.lower())
        else:
            result += el
    return result


print(to_snake("myFancyFunction"))


def to_camel(s: str):
    result = ''
    check = []
    for el in range(len(s)):
        if s[el] == "_":
            result += str(s[el + 1].upper())
            check.append(s[el + 1])
        else:
            if s[el] in check:
                continue
            else:
                result += s[el]
    return result


print(to_camel("my_fancy_function"))


def test_to_snake():
    s = "my_fancy_function"
    assert(to_camel(s) == "myFancyFunction")
    s = "myFancyFunction"
    assert(to_snake(s) == "my_fancy_function")

# print(test_to_snake())
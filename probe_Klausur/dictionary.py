def word_counts(s: str):
    d = dict()
    for el in s.split(" "):
        if el in d:
            d[el] += 1
        else:
            d[el] = 1
    return d



print(word_counts("This sentence is a sentence"))
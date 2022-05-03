from read_files import read_files, read_file
from ignored_words import IGNORED_WORDS
from typing import Any


def remove_header(document: str) -> str:
    return document.split("\n\n")[1]


def normalize_word(s: str) -> str:
    s2 = ""
    for c in s.lower():
        if c.isalpha():
            s2 += c
    return s2


def article_to_words(s: str) -> list[str]:
    words = []
    for w in remove_header(s).split():
        w = normalize_word(w)
        if w not in IGNORED_WORDS:
            words.append(w)
    return words


def count_words(words: list[str]) -> dict[str, int]:
    d = dict()
    for w in words:
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
    return d


def merge_with_plus(d1: dict[str, int], d2: dict[str, int]):
    for k, v in d2.items():
        if k in d1:
            d1[k] += v
        else:
            d1[k] = v


def sort_by_value(d: dict[str, int]) -> list[tuple[int, str]]:
    xs = []
    for k, v in d.items():
        xs.append((v, k))
    xs.sort(reverse=True)
    return xs


def correlated_words(correlations: dict[str, dict[str, int]], words: list[str]):
    for w1 in words:
        for w2 in words:
            if w1 == w2:
                continue
            if w1 not in correlations:
                correlations[w1] = dict()
            if w2 not in correlations[w1]:
                correlations[w1][w2] = 0
            correlations[w1][w2] += 1


def repl(correlations: dict[str, dict[str, int]], word_counts: dict[str, int]):
    while True:
        print()
        w = input("> ")

        if w == ":quit":
            print("Good bye!")
            return

        if w not in word_counts:
            print("Word does not occur in data.")
            continue

        print("The word '" + w + "' was found", word_counts[w], "times.")

        if w not in correlations:
            continue

        print("Top 10 correlations:")
        for i, (count, w2) in enumerate(sort_by_value(correlations[w])):
            if i == 10:
                break
            print("  " + w + " " + w2 + " (" + str(count) + " times)")


if __name__ == '__main__':
    dir_path = input("Enter path of directory to evaluate: ")

    # Read files from disk.
    print()
    files = read_files(dir_path)

    # Count words and search for correlations.
    print()
    print("Computing statistics...")
    word_counts = dict()
    correlations = dict()
    for file in files:
        words = article_to_words(file)
        merge_with_plus(word_counts, count_words(words))
        correlated_words(correlations, words)

    # Print top 10 words.
    word_counts_sorted = sort_by_value(word_counts)
    print()
    print("Top 10 words:")
    for i, (count, word) in enumerate(word_counts_sorted):
        if i == 10:
            break
        print("  " + word + " (" + str(count) + " times)")

    # Enter the REPL to allow the user to search for correlations.
    repl(correlations, word_counts)

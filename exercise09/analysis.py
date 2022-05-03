from read_files import read_files
from ignored_words import IGNORED_WORDS
from collections import Counter


#files = read_files("C:/Users/NXTSHT.KYZ/Nextcloud/EiP/Informatik Aufgaben/exercise09/tagesschau/all")


def remove_header(text: str) -> str:
    result = ""
    header_flag = False
    for line in text.split("\n"):
        if header_flag:
            result += line.strip()
        if line.strip() == "":
            header_flag = True
    return result


def nomarlize_word(text: str) -> str:
    result = ""
    for i in text:
        if i.isalpha() or i == " ":
            result += i.lower()
    return result


def article_to_words(text: str) -> list:
    result = ""
    finalresult = []
    content = remove_header(text)
    for word in content:
            result += nomarlize_word(word)
    new_result = result.split()
    for x in new_result:
        if x not in IGNORED_WORDS:
            finalresult.append(x)
    return finalresult


def count_words(words: list) -> dict:
    word_list = {}
    for word in words:
        try:
            word_list[word] += 1
        except KeyError:
            word_list[word] = 1
    return word_list


def merge_with_plus(d1: dict, d2: dict) -> dict:
    result = {}
    if bool(d1) == False:
        d1.update(d2)
        return d1
    if bool(d1) == True:
        merge = Counter(d1) + Counter(d2)
        for x in merge:
            result.update({x : merge[x]})
    return result     


def sort_by_value(d: dict) -> list:
    result = []
    for word in sorted(d, key = lambda x: d[x], reverse = True):
        result.append((d[word], word))
    return result


def correlated_words(d: dict, list_of_word: list) -> dict:
    if bool(d) == False:
        for word in list_of_word:
            sub_dic = count_words(list_of_word)
            sub_dic.pop(word)
            if word in d:
                d.update({word : merge_with_plus(sub_dic, sub_dic)})
            else:
                d.update({word : sub_dic})
        return d
    if bool(d) == True:
        for word in list_of_word:
            if word in d:
                sub_dic = count_words(list_of_word)
                sub_dic.pop(word)
                d[word] = merge_with_plus(d[word], sub_dic)
            if word not in d:
                sub_dic = count_words(list_of_word)
                sub_dic.pop(word)
                d.update({word : sub_dic})
        return d


if __name__ == '__main__':
    path = input("Enter path of directory to evaluate: ")
    print()
    files = read_files(path)
    print()
    print("Computing statistics...")
    print()
    d = []
    D = {}
    cod = {}
    for file in files:
        new_d = count_words(article_to_words(file))
        cod = correlated_words(cod, article_to_words(file))
        d.append(new_d)
    for dic in d:
        D = merge_with_plus(D, dic)
    sorted_D = sort_by_value(D)
    print("Top 10 words:")
    i = 0
    for x in range(10):
        print("  " + str(sorted_D[i][1]) + " " + "(" + str(sorted_D[i][0]) + " times)")
        i = i + 1
    print()
    while True:
        command = input("> ")
        if command == ':quit':
            break
        else:
            print("The word '" + str(command) + "' was found " + str(D[command]) + " times.")
            print("Top 10 correlations:")
            sorted_cod = sort_by_value(cod[command])
            i = 0
            for x in range(10):
                print("  " + str(command) + " " + str(sorted_cod[i][1]) + " " + "(" + str(sorted_cod[i][0]) + " times)")
                i = i + 1
            print()
    print("Good bye!")
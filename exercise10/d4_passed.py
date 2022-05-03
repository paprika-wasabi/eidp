if __name__ == '__main__':
    result = []
    i = int(input())
    x = 0
    assert(i) <= 1000
    for x in range(i):
        final_word = ''
        count = 0
        j = input()
        line = j.split(" ")
        word = line[0]
        assert(len(line[0])) <= 1000
        for char in line[1]:
            this_word = ''
            if len(final_word) == len(''.join(set(word))):
                break
            if char in line[0]:
                final_word += char
                count = count + 1
            elif char not in line[0]:
                count = count + 1
        result.append(count)
        x = x + 1
    for int in result:
        print(int)
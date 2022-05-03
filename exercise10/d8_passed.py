def g_to_b(input):
    result = []
    for i in range(len(input)):
        if i == 0:
            result.append(input[i])
        if i > 0:
            if input[i] == result[i - 1]:
                result.append(0)
            elif input[i] != result[i - 1]:
                result.append(1)
    return result

def b_to_d(input):
    i = 0
    result = 0
    while i < len(input):
        result += int(input[len(input) - 1 - i]) * pow(2,i)
        i = i + 1
    return result
  
line = input().split(" ")
yesterday = line[1]
gestern = []
today = line[2]
heute = []
for x in yesterday:
    gestern.append(int(x))
for y in today:
    heute.append(int(y))
result = b_to_d(g_to_b(heute)) - b_to_d(g_to_b(gestern))
print(result)
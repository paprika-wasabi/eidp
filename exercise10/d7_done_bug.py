com = []
n = int(input())
assert(n) >= 1
assert(n) <= 10e7
line = input().split(" ")
for value in line:
    com.append(int(value))
for value in range(n):
    assert(com[value]) >= 1
    assert(com[value]) <= 10e8
result = 0
gift = n
com.sort(reverse=False)
for value in range(n):
    if com[value] < gift and com[value] <= gift - result:
        result = result + 1
        continue
    elif max(com) == n:
        result = max(com)
        break
    elif len(com) == 1:
        result = 1
        break
    elif com[value] > gift - value:
        break
    else:
        result = 0
        break
print(result)
print()
result = 0
gift = n
com.sort(reverse=True)
for value in range(n):
    if com[value] > gift:
        continue
    elif com[value] <= gift - value:
        result = result + gift - value
        break
    if value == n - 1 and com[value] > 1:
        # print(value)
        result = 0
# print(com)
print(result)

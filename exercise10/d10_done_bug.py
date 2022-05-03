# def getKey(item):
#     return item[0]
t = int(input())
assert(t) <= 1000
tc = []
for case in range(t + 1):
    if case == t:break
    # avg_price = []
    com = []
    val = [] #memonization
    n = int(input())
    assert(n) >= 1
    assert(n) <= 1000
    rendeer = input().split()
    for value in rendeer:
        com.append(int(value))
    for i in range(n + 1):
        val.append(0)
    # for value in com:
    #     assert(value) >= 0
    #     assert(value) <= 10e6
    # j = 1
    # for group in com:
    #     price_per = group / j
    #     avg_price.append((price_per, j))
    #     j = j + 1
    # sorted_price = sorted(avg_price, key=getKey, reverse=True)
    # # sold = 0
    # wallet = 0
    # for group in sorted_price:
    #     if group[1] <= n - sold:
    #         money = group[1] * group[0]
    #         sold = sold + group[1]
    #         wallet = wallet + money

    # sell = 0
    # for group in sorted_price:
    #     if sell < n:
    #         for i in range(group[1]):
    #             if sell != n:
    #                 wallet = wallet + group[0]
    #                 sell = sell + 1
    #     elif sell == n:
    #         break
    for i in range(1, n + 1):
        result= 0
        for k in range(i):
            result = max(result, com[k] + val[i - k - 1])
        val[i] = result
    # wallet = val[n]
    tc.append(val[n])
    print(int(tc[case]))
# for i in range(t):
    # print(int(tc[case]))
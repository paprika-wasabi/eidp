t = int(input())
Test_case = []
Result = []
for k in range(t):
    if k == 0:
        pass
    else:
        emt = input()
    fabrick = []
    rendeer = []
    n, r = input().split(" ")
    n = int(n)
    r = int(r)
    for line in range(n):
        f = int(input())
        fabrick.append(f)
        rendeer.append(1)
    for i in range(r - n):
        max_fab = 0
        max_idx = 0
        for j in range(n):
            if fabrick[j] / rendeer[j] > max_fab:
                max_fab = fabrick[j] / rendeer[j]
                max_idx = j
        rendeer[max_idx] += 1
    result = 0
    for j in range(n):
        if fabrick[j] / rendeer[j] > result:
            result = fabrick[j] / rendeer[j]    
    Result.append(result)


for i in range(t):
    print("Case #" + str(i + 1) + ":" + " " + str(int(Result[i])))

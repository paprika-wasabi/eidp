test_case = []
i = int(input())
for num in range(i):
    resort = []
    n, m = input().split(" ")
    m = int(m)
    n = int(n)
    resort.append([n, m])
    for num in range(m):
        pisten = input().split(" ")
        resort.append(pisten)
    test_case.append(resort)

k = []
for resort in range(len(test_case)):
    for ski_area in range(len(test_case[resort])):
        # if resort <= test_case[resort][0][0]:
        for pos in range(len(test_case[resort][ski_area])):
            if ski_area > 0:
                pass
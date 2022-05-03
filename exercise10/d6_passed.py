d, s, r, x, y = input().split()
d, s, r, x, y = int(d), int(s), int(r), int(x), int(y)
assert(d) >= 1
assert(d) <= 10e9
assert(r) < s
assert(r) >= 1
assert(r) <= 10e9
assert(abs(x)) <= 10e9
assert(abs(y)) <= 10e9
dis = s - r
c = pow(pow(x,2) + pow(y,2), 0.5)
dis = dis - c
if d >= dis:
    print("Erfrischung pur")
elif dis > d:
    print("Pech gehabt")







# for value in range(n): for ex.7
#     if com[value] > gift:
#         continue
#     elif com[value] <= gift - value:
#         result = result + gift - value
#         break
#     else:
#         result = 0
# print(result)
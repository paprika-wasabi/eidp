n = 0
m = 0
while n < 3:
    for m in range(0, 3):
        print("O", end='')
    print()
    n = n + 1

print((("X" * 3) + "\n") * 3)
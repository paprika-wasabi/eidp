v, h, d = input().split()
v = int(v)
h = int(h)
area = v / h
d = int(d)
if d >= pow(area, 0.5):
    print("Weihnachten faellt ins Wasser")
else:
    print("Es gibt Geschenke")
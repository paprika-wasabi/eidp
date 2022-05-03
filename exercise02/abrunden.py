from math import floor
Kommazahl = float(input("Kommazahl: "))
Quadriert = Kommazahl ** 2
print("Quadriert:", Quadriert)

Methode1 = round(Quadriert, 0)
print("Methode 1:", Methode1)

Methode2 = float(floor(Quadriert))
print("Methode 2:", Methode2)

x = Quadriert % 1
Methode3 = (Quadriert - x)
print("Methode 3:", Methode3)


\\Solution down below
z = float(input("Kommazahl: "))
q = z ** 2
print("Quadriert:", str(q))

e1 = float(int(q))
print("Methode 1:", e1)

e2 = q // 1
print("Methode 2:", e2)

e3 = q - q % 1
print("Methode 3:", e3)

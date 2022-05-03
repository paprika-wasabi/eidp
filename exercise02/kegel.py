import math
Radius = float(input("Radius: "))
Höhe = float(input("Höhe: "))
x = math.sqrt((Radius * Radius) + (Höhe * Höhe))
sidearea = x * math.pi * Radius
sidearea = round(sidearea, 2)
print("Mantelfläche:", sidearea)

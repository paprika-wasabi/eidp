from cone_area_lib import cone_area
R = float(input("Radius: "))
H = float(input("Höhe: "))
cone_area(R, H)
new_S = round(cone_area(R, H), 2)
print("Mantelfläche:", new_S)
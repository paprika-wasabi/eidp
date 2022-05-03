
def celsius_to_fahrenheit(Cel):
    Fah = (Cel * 1.8) + 32
    return Fah


def fahrenheit_to_celsius(Fah):
    Cel = (Fah - 32) * (5 / 9)
    return Cel


def celsius_to_kelvin(Cel):
    Kev = Cel + 273.15
    return Kev


def kelvin_to_celsius(Kev):
    Cel = Kev - 273.15
    return Cel


def fahrenheit_to_kelvin(Fah):
    Cel = fahrenheit_to_celsius(Fah)
    Kev = celsius_to_kelvin(Cel)
    return Kev


def kelvin_to_fahrenheit(Kev):
    Cel = kelvin_to_celsius(Kev)
    Fah = celsius_to_fahrenheit(Cel)
    return Fah


sourceunit = input("Enter source unit [C / F / K]: ")
sourcevalue = float(input("Enter source value: "))
target = input("Enter target unit [C / F / K]: ")


def temptran(sourceunit, sourcevalue, target):
    if sourceunit == "C" and target == "F":
        Cel = sourcevalue
        output = celsius_to_fahrenheit(Cel)
    elif sourceunit == "C" and target == "K":
        Cel = sourcevalue
        output = celsius_to_kelvin(Cel)
    elif sourceunit == "F" and target == "C":
        Fah = sourcevalue
        output = fahrenheit_to_celsius(Fah)
    elif sourceunit == "F" and target == "K":
        Fah = sourcevalue
        output = fahrenheit_to_kelvin(Fah)
    elif sourceunit == "K" and target == "C":
        Kev = sourcevalue
        output = kelvin_to_celsius(Kev)
    elif sourceunit == "K" and target == "F":
        Kev = sourcevalue
        output = kelvin_to_fahrenheit(Kev)
    else:
        print("falsche Eingabe")
    return output


if __name__ == "__main__":
    print(sourcevalue, sourceunit, "corresponds to", round(temptran(sourceunit, sourcevalue, target), 2), target + ".")
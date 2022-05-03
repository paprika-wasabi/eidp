from dataclasses import dataclass


@dataclass
class Fahrzeug:
    Zustand: int
    Neupreis: int
    Leergewicht: int
    Baujahr: int

    def __post_init__(self):
        assert(self.Zustand) >= 0, "Zustand " + str(self.Zustand) + "% muss zwischen 0% und 100% liegen."
        assert(self.Zustand) <= 100, "Zustand " + str(self.Zustand) + "% muss zwischen 0% und 100% liegen."
        assert(self.Neupreis) >= 0, "Neupreis " + str(self.Neupreis) + "€ muss mindestens 0€ sein."
        assert(self.Leergewicht) > 0, "Leergewicht " + str(self.Leergewicht) + "kg muss größer als 0kg sein."
        assert(self.Baujahr) > 1900, "Baujahr " + str(self.Baujahr) + " muss größer als 1900 sein."

    def gewicht(self) -> int:
        return int(self.Leergewicht)

    def maut(self) -> int:
        raise NotImplementedError

    def alter(self) -> int:
        if self.Baujahr > 2021:
            return 0
        else:
            return 2021 - self.Baujahr

    def markwert(self) -> int:
        result = int(((self.Zustand - (5 * self.alter())) / 100) * self.Neupreis)
        if result < 0:
            return 0
        else:
            return result


@dataclass
class Kraftfahrzeug(Fahrzeug):
    Leistung: int
    Anzahl_Sitzplätze: int

    def __post_init__(self):
        super().__post_init__()
        assert(self.Leistung) > 0, "Leistung " + str(self.Leistung) + "kW muss größer als 0kW sein."
        assert(self.Anzahl_Sitzplätze) > 0, "Sitzplätze " + str(self.Anzahl_Sitzplätze) + " muss größer als 0 sein."

    def plaetze(self) -> int:
        return self.Anzahl_Sitzplätze

    def maut(self) -> int:
        return round(self.gewicht() / 5,) + (self.plaetze() * 25)


@dataclass
class Bus(Kraftfahrzeug):
    Anzahl_Stehplätze: int

    def __post_init__(self):
        super().__post_init__()
        assert(self.Anzahl_Stehplätze) <= self.Anzahl_Sitzplätze, "Stehplätze " + str(self.Anzahl_Stehplätze) + " muss kleiner oder gleich Sitzplätze " + str(self.Anzahl_Sitzplätze) + " sein."
        assert(self.Anzahl_Stehplätze) >= 0

    def plaetze(self) -> int:
        return super().plaetze() + self.Anzahl_Stehplätze


@dataclass
class Fahrrad(Fahrzeug):
    rahmengroesse: int

    def __post_init__(self):
        super().__post_init__()
        assert(self.rahmengroesse) > 0, "Rahmengröße " + str(self.rahmengroesse) + " muss größer als 0cm sein."

    def markwert(self) -> int:
        return int(super().markwert() / 2)

    def maut(self) -> int:
        return 0


@dataclass
class PKW(Kraftfahrzeug):
    pass


@dataclass
class LKW(Kraftfahrzeug):
    Zuladung: int

    def __post_init__(self):
        super().__post_init__()
        assert(self.Zuladung) > 0, "Zuladung " + str(self.Zuladung) + " muss größer als 0kg und maximal " + str(2 * self.Leergewicht) + " sein."
        assert(self.Zuladung) < (2 * self.Leergewicht), "Zuladung " + str(self.Zuladung) + " muss größer als 0kg und maximal " + str(2 * self.Leergewicht) + " sein."

    def maut(self) -> int:
        return super().maut() * 2
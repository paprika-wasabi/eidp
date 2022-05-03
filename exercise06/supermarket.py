from dataclasses import dataclass


@dataclass
class Food:
    expiration_date: str


@dataclass
class NonFood:
    pass


@dataclass
class Stock:
    name: str
    units: int
    price_per_unit: float
    kind: Food | NonFood


def is_expired(Lagerbestand: Stock, Datum) -> str:
    match Lagerbestand.kind:
        case[Food()]:
            if Datum == Food.expiration_date:
                return str(Stock.name + "is expired")
        case[NonFood()]:
            pass


def get_expired(stocks: list[Stock], Datum: str) -> list:
    result = []
    for x in stocks:
        if x.kind != NonFood():
            if x.kind.expiration_date < Datum:
                result.append(x)
    return result


def buy(stock: Stock, Stückzahl: int):
    gekaufte_Ware: int
    gekaufte_Ware = 0
    if stock.units != 0 and stock.units >= Stückzahl:
        stock.units -= Stückzahl
        gekaufte_Ware += Stückzahl
        return gekaufte_Ware

    elif stock.units == 0:
        return "Die Ware ist leide ausverkauft"

    elif stock.units < Stückzahl:
        gekaufte_Ware += stock.units
        stock.units -= gekaufte_Ware
        return gekaufte_Ware
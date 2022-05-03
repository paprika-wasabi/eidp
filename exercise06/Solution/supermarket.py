from dataclasses import dataclass


# Data Types ##################################################################

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
    price_per_unit: int
    kind: Food | NonFood


# Functions ###################################################################

def is_expired(stock: Stock, today: str) -> bool:
    match stock.kind:
        case Food(expiration_date):
            return today > expiration_date
        case NonFood():
            return False


def get_expired(stocks: list[Stock], today: str) -> list[Stock]:
    expired = []
    for stock in stocks:
        if is_expired(stock, today):
            expired += [stock]
    return expired


def buy(stock: Stock, units: int) -> int:
    bought_units = min(stock.units, units)
    stock.units -= bought_units
    return bought_units

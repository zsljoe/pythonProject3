from abc import ABC, abstractmethod


class Szoba(ABC):

    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar


class EgyagyasSzoba(Szoba):
    pass


class KetagyasSzoba(Szoba):
    pass


class Szalloda:

    def __init__(self, name: str):
        self.name = name


class Foglalas:
    pass

Szalloda = Szalloda("Toparti")
Egyagyas = EgyagyasSzoba(101,30000)
Ketagyas = KetagyasSzoba(102,40000)


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

    def __str__(self):
        return f"A szálloda neve {self.name}"


Elso_szalloda = Szalloda("Toparti")

print(Elso_szalloda)






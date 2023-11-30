from abc import ABC, abstractmethod

class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar


class EgyagyasSzoba(Szoba):
    def __init__(self,szobaszam, ar):
        szobaszam = 101
        ar = 30000

class KetagyasSzoba(Szoba):
    def __init__(self,szobaszam, ar):
        szobaszam = 102
        ar = 40000
class Szalloda:

    def __init__(self, name: str):
        self.name = name


class Foglalas:
    def __str__(self):
        foglalasok_str = self.foglalas_datumok()

Szalloda = Szalloda("Toparti")




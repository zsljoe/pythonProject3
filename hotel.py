from abc import ABC, abstractmethod


class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar


class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam, ar):
        self.szobaszam = 101
        self.ar = 30000


class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam, ar):
        self.szobaszam = 102
        self.ar = 40000


class Szalloda:

    def __init__(self, szobak, name: str):
        self.szobak = []
        self.name = name

    def szoba_hozzaadas(self, szoba: Szoba):
        self.szobak.append(szoba)


    def szobakletrehozasa(self):
        self.szoba_hozzaadas(EgyagyasSzoba)
        self.szoba_hozzaadas(KetagyasSzoba)


class Foglalas:
    def __str__(self):
        foglalasok_str = self.foglalas_datumok()
        return f"Fogalalás dátuma: {foglalasok_str}"



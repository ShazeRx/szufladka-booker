from fasady.fasada_ksiazek.fasada_ksiazki import FasadaKsiazki
from przypadki_uzycia.blad import Blad
from przypadki_uzycia.i_przypadek_uzycia import IPrzypadekUzycia


class WyswietlKsiazkiWSzufladce(IPrzypadekUzycia):
    def __init__(self, fasada_ksiazki: FasadaKsiazki):
        self.fasada_ksiazki = fasada_ksiazki

    def wykonaj(self) -> None or Blad:
        return self.fasada_ksiazki.pokaz_ksiazki_w_szufladce()

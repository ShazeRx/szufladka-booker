from fasady.fasada_ksiazek.fasada_ksiazki import FasadaKsiazki
from modele.ksiazka.model_ksiazka import ModelKsiazki
from przypadki_uzycia.blad import Blad
from przypadki_uzycia.i_przypadek_uzycia import IPrzypadekUzycia


class DodajKsiazkePrzypadekUzycia(IPrzypadekUzycia):
    def __init__(self, fasada_ksiazki: FasadaKsiazki):
        self.fasada_ksiazki = fasada_ksiazki

    def wykonaj(self, model_ksiazki: ModelKsiazki) -> None or Blad:
        return self.fasada_ksiazki.dodaj_ksiazke(model_ksiazki)

from fasady.uzytkownicy.fasada_uzytkownika import FasadaUzytkownika
from modele.uzytkownik.model_uzytkownika import ModelUzytkownika
from przypadki_uzycia.blad import Blad
from przypadki_uzycia.i_przypadek_uzycia import IPrzypadekUzycia


class WyswietlProfilPrzypadekUzycia(IPrzypadekUzycia):
    def __init__(self, fasada_uzytkownika: FasadaUzytkownika):
        self.fasadaUzytkownika = fasada_uzytkownika

    def wykonaj(self) -> ModelUzytkownika or Blad:
        return self.fasadaUzytkownika.wyswietl_profil()

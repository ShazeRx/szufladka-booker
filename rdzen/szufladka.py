from dependency_injector.wiring import Provide, inject

from modele.uzytkownik.model_uzytkownika import ModelUzytkownika
from przypadki_uzycia.autoryzacja.zaloguj import ZalogujPrzypadekUzycia
from rdzen.wstrzykiwacz_zaleznosci.kontener_wstrzykiwania import WstrzykiwaczZaleznosci


class Szufladka:

    @inject
    def uruchom(self, zaloguj: ZalogujPrzypadekUzycia = Provide[
        WstrzykiwaczZaleznosci.przypadki_uzycia.zaloguj_przypadek_uzycia]):
        result = zaloguj.wykonaj(ModelUzytkownika("imie", "nazwisko", "email", haslo="haslo"))
        print(result)

    def _show_login_screen(self):
        pass

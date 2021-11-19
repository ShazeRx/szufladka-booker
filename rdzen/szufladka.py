from dependency_injector.wiring import Provide, inject

from interfejs.interfejs_kontroler import InterfejsKontroler
from modele.uzytkownik.model_uzytkownika import ModelUzytkownika
from przypadki_uzycia.uzytkownik.zaloguj import ZalogujPrzypadekUzycia
from rdzen.wstrzykiwacz_zaleznosci.kontener_wstrzykiwania import WstrzykiwaczZaleznosci


class Szufladka:
    @inject
    def test_api(self, zaloguj: ZalogujPrzypadekUzycia = Provide[
        WstrzykiwaczZaleznosci.przypadki_uzycia.zaloguj_przypadek_uzycia]):
        model = ModelUzytkownika(kryptonim="cos", haslo="cos")
        wynik = zaloguj.wykonaj(model_uzytkownika=model)

    def uruchom(self):
        # self.test_api()
        InterfejsKontroler().run()

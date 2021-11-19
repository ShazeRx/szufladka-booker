from przypadki_uzycia.uzytkownik.zaloguj import ZalogujPrzypadekUzycia


class EkranLogowania:
    def __init__(self, zaloguj_przypadek_uzycia: ZalogujPrzypadekUzycia):
        self.zaloguj_przypadek_uzycia = zaloguj_przypadek_uzycia

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def wyswietl_ekran(self):
        pass

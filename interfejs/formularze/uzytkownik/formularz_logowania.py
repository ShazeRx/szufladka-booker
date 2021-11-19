import npyscreen

from modele.uzytkownik.model_uzytkownika import ModelUzytkownika
from przypadki_uzycia.blad import Blad
from przypadki_uzycia.uzytkownik.zaloguj import ZalogujPrzypadekUzycia


class FormularzLogowania(npyscreen.FormBaseNew):
    def __init__(self, zaloguj_przypadek_uzycia: ZalogujPrzypadekUzycia, *args, **keywords):
        super().__init__(*args, **keywords)
        self.zaloguj_przypadek_uzycia = zaloguj_przypadek_uzycia

    def create(self):
        super(FormularzLogowania, self).create()
        self.name = "Logowanie"
        self.kryptonim = self.add(npyscreen.TitleText, name="Kryptonim")
        self.haslo = self.add(npyscreen.TitlePassword, name="Haslo")
        self.przycisk_logowania = self.add(npyscreen.ButtonPress, name="Zaloguj", when_pressed_function=self.zaloguj)
        self.przycisk_rejestracji = self.add(npyscreen.ButtonPress, name="Rejestracja",
                                             when_pressed_function=self.pokaz_rejestracje)

    def zaloguj(self):
        model_uzytkownika = ModelUzytkownika(kryptonim=self.kryptonim.get_value(), haslo=self.haslo.get_value())
        wynik = self.zaloguj_przypadek_uzycia.wykonaj(model_uzytkownika)
        if not isinstance(wynik, Blad):
            self.pokaz_ekran_glowny()
            return
        npyscreen.notify_confirm("Zly kryptonim lub haslo")

    def pokaz_rejestracje(self):
        self.parentApp.zmien_ekran("REJESTRACJA")

    def pokaz_ekran_glowny(self):
        self.parentApp.zmien_ekran("EKRAN_GLOWNY")

import npyscreen

from modele.uzytkownik.model_uzytkownika import ModelUzytkownika
from przypadki_uzycia.blad import Blad
from przypadki_uzycia.uzytkownik.zarejestruj import ZarejestrujPrzypadekUzycia


class FormularzRejestracja(npyscreen.FormBaseNew):
    def __init__(self, rejestracja_przypadek_uzycia: ZarejestrujPrzypadekUzycia, *args, **keywords):
        super().__init__(*args, **keywords)
        self.rejestracja_przypadek_uzycia = rejestracja_przypadek_uzycia

    def create(self):
        super(FormularzRejestracja, self).create()
        self.name = "Rejestracja"
        self.kryptonim = self.add(npyscreen.TitleText, name="Kryptonim")
        self.email = self.add(npyscreen.TitleText, name="Email")
        self.haslo = self.add(npyscreen.TitlePassword, name="Haslo")
        self.przycisk_rejestruj = self.add(npyscreen.ButtonPress, name="Rejestruj",
                                           when_pressed_function=self.rejestruj)
        self.przycisk_powrot = self.add(npyscreen.ButtonPress, name="Powrot do logowania",
                                        when_pressed_function=self.powrot)

    def rejestruj(self):
        model_uzytkownika = ModelUzytkownika(kryptonim=self.kryptonim.get_value(), email=self.email.get_value(),
                                             haslo=self.haslo.get_value())
        wynik = self.rejestracja_przypadek_uzycia.wykonaj(model_uzytkownika)
        if not isinstance(wynik, Blad):
            pass
        npyscreen.notify_confirm("Cos poszło nie tak")

    def powrot(self):
        self.parentApp.zmien_ekran("MAIN")

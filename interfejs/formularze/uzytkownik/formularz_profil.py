import npyscreen

from przypadki_uzycia.blad import Blad
from przypadki_uzycia.uzytkownik.wyswietl_profil import WyswietlProfilPrzypadekUzycia


class FormularzProfil(npyscreen.ActionFormMinimal):
    OK_BUTTON_TEXT = "Powrot"

    def __init__(self, wyswietl_profil_przypadek_uzycia: WyswietlProfilPrzypadekUzycia, *args, **keywords):
        super().__init__(*args, **keywords)
        self.wyswietl_profil_przypadek_uzycia = wyswietl_profil_przypadek_uzycia

    def create(self):
        self.name = "Moj profil"
        self.kryptonim = self.add(npyscreen.TitleText, name="Kryptonim: ", editable=False)
        self.email = self.add(npyscreen.TitleText, name="Email: ", editable=False)

    def while_editing(self, *args, **keywords):
        self.pobierz_dane_uzytkownika()

    def pobierz_dane_uzytkownika(self):
        wynik = self.wyswietl_profil_przypadek_uzycia.wykonaj()
        if not isinstance(wynik, Blad):
            self.kryptonim.value = wynik.kryptonim
            self.email.value = wynik.email
            return
        npyscreen.notify_confirm("Cos poszlo nie tak")

    def on_ok(self):
        self.parentApp.zmien_ekran("EKRAN_GLOWNY")

import npyscreen

from interfejs.widgety.szczegoly_ksiazki import FormularzSzczegolyKsiazki
from przypadki_uzycia.blad import Blad
from przypadki_uzycia.ksiazki.oddaj_ksiazke import OddajKsiazkePrzypadekUzycia


class FormularzSzczegolyKsiazkiMoje(FormularzSzczegolyKsiazki):
    def __init__(self, oddaj_ksiazke: OddajKsiazkePrzypadekUzycia, *args, **keywords):
        self.oddaj_ksiazke = oddaj_ksiazke
        super().__init__(przypadek_uzycia=oddaj_ksiazke, *args, **keywords)

    OK_BUTTON_TEXT = "Oddaj"

    def on_ok(self):
        wynik = self.oddaj_ksiazke.wykonaj(indeks=self.indeks.value)
        if isinstance(wynik, Blad):
            npyscreen.notify_confirm("Wystapil blad przy oddawaniu", form_color='DANGER')
            return
        npyscreen.notify_confirm("Oddano", form_color='GOODHL')
        self.on_cancel()

    def on_cancel(self):
        self.parentApp.zmien_ekran("MOJE_KSIAZKI")

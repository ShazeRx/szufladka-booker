import npyscreen

from interfejs.widgety.szczegoly_ksiazki import FormularzSzczegolyKsiazki
from przypadki_uzycia.blad import Blad
from przypadki_uzycia.ksiazki.wez_ksiazke import WezKsiazkePrzypadekUzycia


class FormularzSzczegolyKsiazkiSzufladka(FormularzSzczegolyKsiazki):
    def __init__(self, wez_ksiazke: WezKsiazkePrzypadekUzycia, *args, **keywords):
        self.wez_ksiazke = wez_ksiazke
        super().__init__(przypadek_uzycia=wez_ksiazke, *args, **keywords)

    OK_BUTTON_TEXT = "Wypozycz"

    def on_ok(self):
        wynik = self.wez_ksiazke.wykonaj(indeks=self.indeks.value)
        if isinstance(wynik, Blad):
            npyscreen.notify_confirm("Wystapil blad przy oddawaniu")
            return
        self.on_cancel()

    def on_cancel(self):
        self.parentApp.zmien_ekran("EKRAN_GLOWNY")

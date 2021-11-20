import npyscreen

from modele.ksiazka.model_ksiazka import ModelKsiazki
from przypadki_uzycia.blad import Blad
from przypadki_uzycia.ksiazki.dodaj_ksiazke import DodajKsiazkePrzypadekUzycia


class FormularzDodawaniaKsiazki(npyscreen.ActionPopupWide):
    def __init__(self, dodaj_ksiazke: DodajKsiazkePrzypadekUzycia, *args, **keywords):
        self.dodaj_ksiazke = dodaj_ksiazke
        super().__init__(*args, **keywords)

    OK_BUTTON_TEXT = "Dodaj"
    CANCEL_BUTTON_TEXT = "Anuluj"

    def create(self):
        self.name = "Dodawanie Ksiazki"
        self.tytul = self.add(npyscreen.TitleText, name="Tytul")
        self.autor = self.add(npyscreen.TitleText, name="Autor")
        self.rok_wydania = self.add(npyscreen.TitleText, name="Rok wydania")
        self.wydawnictwo = self.add(npyscreen.TitleText, name="Wydawnictwo")
        self.display()

    def on_ok(self):
        if not self.is_int_parseable(self.rok_wydania.value):
            npyscreen.notify_confirm("Rok wydania musi byc liczba", form_color='DANGER')
            return
        ksiazka = ModelKsiazki(tytul=self.tytul.value, autor=self.autor.value, rok_wydania=self.rok_wydania.value,
                               wydawnictwo=self.wydawnictwo.value)
        wynik = self.dodaj_ksiazke.wykonaj(ksiazka)
        if not isinstance(wynik, Blad):
            npyscreen.notify_confirm("Dodano", form_color='GOODHL')
            self.on_cancel()
            return
        npyscreen.notify_confirm("Cos poszlo nie tak", form_color='DANGER')

    def on_cancel(self):
        self.clear_and_redraw_input()
        self.parentApp.switchForm("EKRAN_GLOWNY")

    def is_int_parseable(self, value: str) -> bool:
        try:
            int(value)
            return True
        except ValueError:
            return False

    def clear_and_redraw_input(self):
        self.tytul.value = None
        self.autor.value = None
        self.wydawnictwo.value = None
        self.rok_wydania.value = None
        self.display()

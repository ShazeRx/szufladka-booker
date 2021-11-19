import curses

import npyscreen

from przypadki_uzycia.blad import Blad
from przypadki_uzycia.ksiazki.wyswietl_moje_ksiazki import WyswietlMojeKsiazkiPrzypadekUzycia


class FormularzMojeKsiazki(npyscreen.ActionFormMinimal):
    OK_BUTTON_TEXT = "Powrot"

    def __init__(self, moje_ksiazki: WyswietlMojeKsiazkiPrzypadekUzycia, *args, **keywords):
        self.moje_ksiazki = moje_ksiazki
        self.ksiazki = [[]]
        super().__init__(*args, **keywords)

    def while_editing(self, *args, **keywords):
        self.pobierz_ksiazki()

    def create(self):
        self.name = "Moje Ksiazki"
        if (len(self.ksiazki) != 0):
            self.grid = self.add(npyscreen.GridColTitles, name="Moje ksiazki",
                                 col_titles=["Indeks", "Tytul", "Autor", "Rok Wydania", "Wydawnicto"], columns=5)
            self.grid.values = self.ksiazki
            self.grid.add_handlers({curses.ascii.NL: self.wyswietl_szczegoly_ksiazki})

        else:
            self.add(npyscreen.Textfield, message="Brak ksiazek w szufladce")

    def pobierz_ksiazki(self):
        ksiazki = self.moje_ksiazki.wykonaj()
        if not isinstance(ksiazki, Blad):
            self.ksiazki = [[ksiazka.indeks, ksiazka.tytul, ksiazka.autor, ksiazka.rok_wydania, ksiazka.wydawnictwo] for
                            ksiazka in
                            ksiazki]
            self.grid.values = self.ksiazki
            self.grid.display()

    def wyswietl_szczegoly_ksiazki(self, input):
        zaznaczona_ksiazka = self.grid.selected_row()
        if len(zaznaczona_ksiazka) != 0:
            self.parentApp.getForm("SZCZEGOLY_KSIAZKI_MOJE").indeks.value = str(zaznaczona_ksiazka[0])
            self.parentApp.getForm("SZCZEGOLY_KSIAZKI_MOJE").tytul.value = zaznaczona_ksiazka[1]
            self.parentApp.getForm("SZCZEGOLY_KSIAZKI_MOJE").autor.value = zaznaczona_ksiazka[2]
            self.parentApp.getForm("SZCZEGOLY_KSIAZKI_MOJE").rok_wydania.value = zaznaczona_ksiazka[3]
            self.parentApp.getForm("SZCZEGOLY_KSIAZKI_MOJE").wydawnictwo.value = zaznaczona_ksiazka[4]
            self.parentApp.zmien_ekran("SZCZEGOLY_KSIAZKI_MOJE")

    def on_ok(self):
        self.parentApp.zmien_ekran("EKRAN_GLOWNY")

import curses
import sys

import npyscreen

from przypadki_uzycia.blad import Blad
from przypadki_uzycia.ksiazki.wyswietl_ksiazki_w_szufladce import WyswietlKsiazkiWSzufladce


class EkranGlowny(npyscreen.FormWithMenus):
    def __init__(self, pokaz_ksiazki_w_szufladce: WyswietlKsiazkiWSzufladce, *args, **keywords):
        self.pokaz_ksiazki_w_szufladce = pokaz_ksiazki_w_szufladce
        self.ksiazki = [[]]
        super().__init__(*args, **keywords)

    def while_editing(self, *args, **keywords):
        self.pobierz_ksiazki()

    def create(self):
        self.name = "Szufladka"
        self.add(npyscreen.TitleText, name="Porada: ",
                 value="Kliknij enter na zaznaczonej pozycji aby przejsc do szczegolow", editable=False)
        self.menu = self.add_menu(name="Menu Glowne", shortcut="^M")
        self.menu.addItem(text="Dodaj Ksiazke", onSelect=self.dodawanie_produktu)
        self.menu.addItem(text="Moje Ksiazki", onSelect=self.wyswietl_moje_ksiazki)
        self.menu.addItem(text="Moj profil", onSelect=self.wyswietl_profil)
        self.menu.addItem(text="Wyjdz", onSelect=self.zamknij_aplikacje)
        if (len(self.ksiazki) != 0):
            self.grid = self.add(npyscreen.GridColTitles, name="Ksiazki w szufladce",
                                 col_titles=["Indeks", "Tytul", "Autor", "Rok Wydania", "Wydawnicto"], columns=5)
            self.grid.values = self.ksiazki
            self.grid.add_handlers({curses.ascii.NL: self.wyswietl_szczegoly_ksiazki})

        else:
            self.add(npyscreen.Textfield, message="Brak ksiazek w szufladce")

    def dodawanie_produktu(self):
        self.parentApp.zmien_ekran("DODAWANIE_KSIAZKI")

    def pobierz_ksiazki(self):
        ksiazki = self.pokaz_ksiazki_w_szufladce.wykonaj()
        if not isinstance(ksiazki, Blad):
            self.ksiazki = [[ksiazka.indeks, ksiazka.tytul, ksiazka.autor, ksiazka.rok_wydania, ksiazka.wydawnictwo] for
                            ksiazka in
                            ksiazki]
            self.grid.values = self.ksiazki
            self.grid.display()
            return
        npyscreen.notify_confirm("Cos poszlo nie tak")

    def wyswietl_profil(self):
        self.parentApp.zmien_ekran("PROFIL")

    def zamknij_aplikacje(self):
        sys.exit(0)

    def wyswietl_szczegoly_ksiazki(self, input):
        zaznaczona_ksiazka = self.grid.selected_row()
        if len(zaznaczona_ksiazka) != 0:
            self.parentApp.getForm("SZCZEGOLY_KSIAZKI_SZUFLADKA").indeks.value = str(zaznaczona_ksiazka[0])
            self.parentApp.getForm("SZCZEGOLY_KSIAZKI_SZUFLADKA").tytul.value = zaznaczona_ksiazka[1]
            self.parentApp.getForm("SZCZEGOLY_KSIAZKI_SZUFLADKA").autor.value = zaznaczona_ksiazka[2]
            self.parentApp.getForm("SZCZEGOLY_KSIAZKI_SZUFLADKA").rok_wydania.value = zaznaczona_ksiazka[3]
            self.parentApp.getForm("SZCZEGOLY_KSIAZKI_SZUFLADKA").wydawnictwo.value = zaznaczona_ksiazka[4]
            self.parentApp.zmien_ekran("SZCZEGOLY_KSIAZKI_SZUFLADKA")

    def wyswietl_moje_ksiazki(self):
        self.parentApp.zmien_ekran("MOJE_KSIAZKI")

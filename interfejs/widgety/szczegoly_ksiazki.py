import npyscreen

from przypadki_uzycia.i_przypadek_uzycia import IPrzypadekUzycia


class FormularzSzczegolyKsiazki(npyscreen.ActionFormExpandedV2):
    CANCEL_BUTTON_TEXT = "Powrot"

    def __init__(self, przypadek_uzycia: IPrzypadekUzycia, *args, **keywords):
        self.przypadek_uzycia = przypadek_uzycia
        super().__init__(*args, **keywords)

    def create(self):
        self.name = "Szczegoly ksiazki"
        self.indeks = self.add(npyscreen.TitleText, name="Indeks: ", editable=False)
        self.tytul = self.add(npyscreen.TitleText, name="Tytul: ", editable=False)
        self.autor = self.add(npyscreen.TitleText, name="Autor: ", editable=False)
        self.rok_wydania = self.add(npyscreen.TitleText, name="Rok Wydania: ", editable=False)
        self.wydawnictwo = self.add(npyscreen.TitleText, name="Wydawnictwo:", editable=False)

    def on_ok(self):
        raise NotImplementedError()

    def on_cancel(self):
        raise NotImplementedError()

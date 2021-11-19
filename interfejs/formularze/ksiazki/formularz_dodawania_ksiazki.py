import npyscreen


class FormularzDodawaniaKsiazki(npyscreen.ActionPopupWide):
    OK_BUTTON_TEXT = "Dodaj"
    CANCEL_BUTTON_TEXT = "Anuluj"

    def create(self):
        self.name = "Dodawanie Ksiazki"
        self.add(npyscreen.TitleText, name="Tytul")
        self.add(npyscreen.TitleText, name="Autor")
        self.add(npyscreen.TitleText, name="Data wydania")
        self.add(npyscreen.TitleText, name="Wydawnictwo")
        self.display()

    def on_cancel(self):
        self.parentApp.switchForm("EKRAN_GLOWNY")

import npyscreen
from dependency_injector.wiring import Provide, inject

from interfejs.formularze.ekran_glowny import EkranGlowny
from interfejs.formularze.ksiazki.formularz_dodawania_ksiazki import FormularzDodawaniaKsiazki
from interfejs.formularze.ksiazki.formularz_moje_ksiazki import FormularzMojeKsiazki
from interfejs.formularze.ksiazki.formularz_szczegoly_ksiazki_moje import FormularzSzczegolyKsiazkiMoje
from interfejs.formularze.ksiazki.formularz_szczegoly_ksiazki_szufladka import FormularzSzczegolyKsiazkiSzufladka
from interfejs.formularze.uzytkownik.formularz_logowania import FormularzLogowania
from interfejs.formularze.uzytkownik.formularz_profil import FormularzProfil
from interfejs.formularze.uzytkownik.formularz_rejestracja import FormularzRejestracja
from przypadki_uzycia.ksiazki.oddaj_ksiazke import OddajKsiazkePrzypadekUzycia
from przypadki_uzycia.ksiazki.wez_ksiazke import WezKsiazkePrzypadekUzycia
from przypadki_uzycia.ksiazki.wyswietl_ksiazki_w_szufladce import WyswietlKsiazkiWSzufladce
from przypadki_uzycia.ksiazki.wyswietl_moje_ksiazki import WyswietlMojeKsiazkiPrzypadekUzycia
from przypadki_uzycia.uzytkownik.wyswietl_profil import WyswietlProfilPrzypadekUzycia
from przypadki_uzycia.uzytkownik.zaloguj import ZalogujPrzypadekUzycia
from przypadki_uzycia.uzytkownik.zarejestruj import ZarejestrujPrzypadekUzycia
from rdzen.wstrzykiwacz_zaleznosci.kontener_wstrzykiwania import WstrzykiwaczZaleznosci


class InterfejsKontroler(npyscreen.NPSAppManaged):

    def onStart(self):
        self.uruchom_z_zaleznosciami()

    @inject
    def uruchom_z_zaleznosciami(self, zaloguj: ZalogujPrzypadekUzycia = Provide[
        WstrzykiwaczZaleznosci.przypadki_uzycia.zaloguj_przypadek_uzycia],
                                rejestracja_przypadek_uzycia: ZarejestrujPrzypadekUzycia = Provide[
                                    WstrzykiwaczZaleznosci.przypadki_uzycia.rejestracja_przypadek_uzycia],
                                pokaz_ksiazki_w_szufladce: WyswietlKsiazkiWSzufladce = Provide[
                                    WstrzykiwaczZaleznosci.przypadki_uzycia.ksiazki_w_szufladce],
                                wyswietl_profil_przypadek_uzycia: WyswietlProfilPrzypadekUzycia = Provide[
                                    WstrzykiwaczZaleznosci.przypadki_uzycia.wyswietl_profil_przypadek_uzycia],
                                wez_ksiazke: WezKsiazkePrzypadekUzycia = Provide[
                                    WstrzykiwaczZaleznosci.przypadki_uzycia.wez_ksiazke],
                                moje_ksiazki: WyswietlMojeKsiazkiPrzypadekUzycia = Provide[
                                    WstrzykiwaczZaleznosci.przypadki_uzycia.moje_ksiazki],
                                oddaj_ksiazke: OddajKsiazkePrzypadekUzycia = Provide[
                                    WstrzykiwaczZaleznosci.przypadki_uzycia.oddaj_ksiazke]):
        self.addForm("MAIN", FormularzLogowania, name="Formularz Logowania",
                     zaloguj_przypadek_uzycia=zaloguj)

        self.addForm("REJESTRACJA", FormularzRejestracja, name="Rejestracja",
                     rejestracja_przypadek_uzycia=rejestracja_przypadek_uzycia)

        self.addForm("EKRAN_GLOWNY", EkranGlowny, name="Eran Glowny",
                     pokaz_ksiazki_w_szufladce=pokaz_ksiazki_w_szufladce)

        self.addForm("DODAWANIE_KSIAZKI", FormularzDodawaniaKsiazki, name="Dodawanie Ksiazki")

        self.addForm("PROFIL", FormularzProfil, name="Profil",
                     wyswietl_profil_przypadek_uzycia=wyswietl_profil_przypadek_uzycia)

        self.addForm("SZCZEGOLY_KSIAZKI_SZUFLADKA", FormularzSzczegolyKsiazkiSzufladka,
                     name="Szczegoly Ksiazki Szufladka",
                     wez_ksiazke=wez_ksiazke)

        self.addForm("SZCZEGOLY_KSIAZKI_MOJE", FormularzSzczegolyKsiazkiMoje, name="Szczegoly Ksiazki Moje",
                     oddaj_ksiazke=oddaj_ksiazke)

        self.addForm("MOJE_KSIAZKI", FormularzMojeKsiazki, name="Moje Ksiazki", moje_ksiazki=moje_ksiazki)

    def zmien_ekran(self, nazwa):
        self.switchForm(nazwa)
        self.resetHistory()

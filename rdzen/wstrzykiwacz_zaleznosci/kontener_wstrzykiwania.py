from dependency_injector import containers, providers

from fasady.fasada_ksiazek.fasada_ksiazki import FasadaKsiazki
from fasady.uzytkownicy.fasada_uzytkownika import FasadaUzytkownika
from http_klient.klient_http import KlientHttp
from przypadki_uzycia.ksiazki.dodaj_ksiazke import DodajKsiazkePrzypadekUzycia
from przypadki_uzycia.ksiazki.oddaj_ksiazke import OddajKsiazkePrzypadekUzycia
from przypadki_uzycia.ksiazki.wez_ksiazke import WezKsiazkePrzypadekUzycia
from przypadki_uzycia.ksiazki.wyswietl_ksiazki_w_szufladce import WyswietlKsiazkiWSzufladce
from przypadki_uzycia.ksiazki.wyswietl_moje_ksiazki import WyswietlMojeKsiazkiPrzypadekUzycia
from przypadki_uzycia.uzytkownik.wyswietl_profil import WyswietlProfilPrzypadekUzycia
from przypadki_uzycia.uzytkownik.zaloguj import ZalogujPrzypadekUzycia
from przypadki_uzycia.uzytkownik.zarejestruj import ZarejestrujPrzypadekUzycia


class KlientKttp(containers.DeclarativeContainer):
    klient_http = providers.Singleton(KlientHttp)


class Fasady(containers.DeclarativeContainer):
    klient_http_kontener = providers.DependenciesContainer()

    fasada_uzytkownik = providers.Factory(FasadaUzytkownika, i_klient_http=klient_http_kontener.klient_http)

    fasada_ksiazki = providers.Factory(FasadaKsiazki, i_klient_http=klient_http_kontener.klient_http)


class PrzypadkiUzycia(containers.DeclarativeContainer):
    fasada_kontener = providers.DependenciesContainer()
    zaloguj_przypadek_uzycia = providers.Factory(ZalogujPrzypadekUzycia,
                                                 fasada_uzytkownika=fasada_kontener.fasada_uzytkownik)
    rejestracja_przypadek_uzycia = providers.Factory(ZarejestrujPrzypadekUzycia,
                                                     fasada_uzytkownika=fasada_kontener.fasada_uzytkownik)
    wyswietl_profil_przypadek_uzycia = providers.Factory(WyswietlProfilPrzypadekUzycia,
                                                         fasada_uzytkownika=fasada_kontener.fasada_uzytkownik)
    ksiazki_w_szufladce = providers.Factory(WyswietlKsiazkiWSzufladce,
                                            fasada_ksiazki=fasada_kontener.fasada_ksiazki)
    wez_ksiazke = providers.Factory(WezKsiazkePrzypadekUzycia, fasada_ksiazki=fasada_kontener.fasada_ksiazki)

    moje_ksiazki = providers.Factory(WyswietlMojeKsiazkiPrzypadekUzycia, fasada_ksiazki=fasada_kontener.fasada_ksiazki)

    oddaj_ksiazke = providers.Factory(OddajKsiazkePrzypadekUzycia, fasada_ksiazki=fasada_kontener.fasada_ksiazki)

    dodaj_ksiazke = providers.Factory(DodajKsiazkePrzypadekUzycia, fasada_ksiazki=fasada_kontener.fasada_ksiazki)


class WstrzykiwaczZaleznosci(containers.DeclarativeContainer):
    klient_http = providers.Container(KlientKttp)

    fasady = providers.Container(Fasady, klient_http_kontener=klient_http)

    przypadki_uzycia = providers.Container(PrzypadkiUzycia, fasada_kontener=fasady)

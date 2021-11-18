from dependency_injector import containers, providers

from fasady.uzytkownicy.fasada_uzytkownika import FasadaUzytkownika
from http_klient.klient_http import KlientHttp
from przypadki_uzycia.autoryzacja.zaloguj import ZalogujPrzypadekUzycia


class KlientKttp(containers.DeclarativeContainer):
    klient_http = providers.Singleton(KlientHttp)


class Fasady(containers.DeclarativeContainer):
    klient_http_kontener = providers.DependenciesContainer()

    fasada_uzytkownik = providers.Factory(FasadaUzytkownika, i_klient_http=klient_http_kontener.klient_http)


class PrzypadkiUzycia(containers.DeclarativeContainer):
    fasada_kontener = providers.DependenciesContainer()
    zaloguj_przypadek_uzycia = providers.Factory(ZalogujPrzypadekUzycia,
                                                 fasada_uzytkownika=fasada_kontener.fasada_uzytkownik)


class WstrzykiwaczZaleznosci(containers.DeclarativeContainer):
    klient_http = providers.Container(KlientKttp)

    fasady = providers.Container(Fasady, klient_http_kontener=klient_http)

    przypadki_uzycia = providers.Container(PrzypadkiUzycia, fasada_kontener=fasady)

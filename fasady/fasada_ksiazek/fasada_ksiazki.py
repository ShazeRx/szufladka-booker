from http_klient.I_klient_http import IKlientHttp
from http_klient.api.api_stale import KSIAZKA_ODDAJ, KSIAZKI_SZUFLADKA, KSIAZKI_MOJE, KSIAZKA_DODAJ
from modele.ksiazka.model_ksiazka import ModelKsiazki, KsiazkaSchemat
from przypadki_uzycia.blad import Blad


class FasadaKsiazki:
    def __init__(self, i_klient_http: IKlientHttp):
        self.i_klient_http = i_klient_http
        self.ksiazka_schemat = KsiazkaSchemat()

    def oddaj_ksiazke(self) -> None or Blad:
        odpowiedz = self.i_klient_http.patch(jwt="jwt", url=KSIAZKA_ODDAJ)
        # TODO: Zrobic response jako obiekt nie jako tupla
        if odpowiedz_kod := odpowiedz[1] != 200:
            return Blad(odpowiedz_kod, odpowiedz[0])
        return None

    def dodaj_ksiazke(self) -> None or Blad:
        odpowiedz = self.i_klient_http.post(jwt="jwt", url=KSIAZKA_DODAJ)
        # TODO: Zrobic response jako obiekt nie jako tupla
        if odpowiedz_kod := odpowiedz[1] != 200:
            return Blad(odpowiedz_kod, odpowiedz[0])
        return None

    def pokaz_ksiazki_w_szufladce(self) -> list[ModelKsiazki] or Blad:
        odpowiedz = self.i_klient_http.get(jwt="jwt", url=KSIAZKI_SZUFLADKA)
        if odpowiedz_kod := odpowiedz[1] != 200:
            return Blad(odpowiedz_kod, odpowiedz[0])
        return self.ksiazka_schemat.loads(many=True, json_data=odpowiedz[0])

    def pokaz_moje_ksiazki(self) -> list[ModelKsiazki] or Blad:
        odpowiedz = self.i_klient_http.get(jwt="jwt", url=KSIAZKI_MOJE)
        if odpowiedz_kod := odpowiedz[1] != 200:
            return Blad(odpowiedz_kod, odpowiedz[0])
        return self.ksiazka_schemat.loads(many=True, json_data=odpowiedz[0])

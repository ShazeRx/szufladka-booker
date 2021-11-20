from http_klient.I_klient_http import IKlientHttp
from http_klient.api.api_stale import KSIAZKA_ODDAJ, KSIAZKI_SZUFLADKA, KSIAZKI_MOJE, KSIAZKA_DODAJ, KSIAZKA_WEZ
from modele.ksiazka.model_ksiazka import ModelKsiazki, KsiazkaSchemat
from przypadki_uzycia.blad import Blad


class FasadaKsiazki:
    def __init__(self, i_klient_http: IKlientHttp):
        self.i_klient_http = i_klient_http
        self.ksiazka_schemat = KsiazkaSchemat()

    def oddaj_ksiazke(self, indeks) -> None or Blad:
        odpowiedz = self.i_klient_http.patch(jwt="jwt", url=KSIAZKA_ODDAJ, params={"indeks": indeks})
        # TODO: Zrobic response jako obiekt nie jako tupla
        if odpowiedz_kod := odpowiedz[1] != 200:
            return Blad(odpowiedz_kod, odpowiedz[0])
        return None

    def dodaj_ksiazke(self, model_ksiazki: ModelKsiazki) -> None or Blad:
        odpowiedz = self.i_klient_http.post(jwt="jwt", url=KSIAZKA_DODAJ,
                                            body=self.ksiazka_schemat.dumps(model_ksiazki))
        # TODO: Zrobic response jako obiekt nie jako tupla
        if odpowiedz_kod := odpowiedz[1] != 200:
            return Blad(odpowiedz_kod, odpowiedz[0])
        return None

    def pokaz_ksiazki_w_szufladce(self) -> list[ModelKsiazki] or Blad:
        odpowiedz = self.i_klient_http.get(jwt="jwt", url=KSIAZKI_SZUFLADKA)
        if odpowiedz_kod := odpowiedz[1] != 200:
            return Blad(odpowiedz_kod, odpowiedz[0])
        return self.ksiazka_schemat.load(many=True, data=odpowiedz[0])

    def pokaz_moje_ksiazki(self) -> list[ModelKsiazki] or Blad:
        odpowiedz = self.i_klient_http.get(jwt="jwt", url=KSIAZKI_MOJE)
        if odpowiedz_kod := odpowiedz[1] != 200:
            return Blad(odpowiedz_kod, odpowiedz[0])
        return self.ksiazka_schemat.load(many=True, data=odpowiedz[0])

    def wez_ksiazke(self, indeks) -> None or Blad:
        odpowiedz = self.i_klient_http.patch(jwt="jwt", url=KSIAZKA_WEZ, params={"indeks": indeks})
        if odpowiedz_kod := odpowiedz[1] != 200:
            return Blad(odpowiedz_kod, odpowiedz[0])
        return None

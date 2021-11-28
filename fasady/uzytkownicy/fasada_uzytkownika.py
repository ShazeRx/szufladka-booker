from http_klient.I_klient_http import IKlientHttp
from http_klient.api.api_stale import LOGOWANIE_ENDPOINT, REJESTRACJA_ENDPOINT, PROFIL_ENDPOINT
from http_klient.narzedzia_http.jwt_opiekun import JwtOpiekun
from modele.uzytkownik.model_jwt import JWTSchemat
from modele.uzytkownik.model_uzytkownika import ModelUzytkownika, UzytkownikSchemat
from przypadki_uzycia.blad import Blad


class FasadaUzytkownika:
    def __init__(self, i_klient_http: IKlientHttp, jwt_opiekun: JwtOpiekun):
        self.i_klient_http = i_klient_http
        self._uzytkownik_schemat = UzytkownikSchemat()
        self._jwt_schemat = JWTSchemat()
        self._jwt_opiekun = jwt_opiekun

    def zaloguj(self, model_uzytkownika: ModelUzytkownika) -> None or Blad:
        odpowiedz = self.i_klient_http.post(body=self._uzytkownik_schemat.dumps(model_uzytkownika),
                                            url=LOGOWANIE_ENDPOINT)
        # TODO: Zrobic response jako obiekt nie jako tupla
        if (odpowiedz_kod := odpowiedz[1]) != 200:
            return Blad(odpowiedz_kod, odpowiedz[0])
        print(odpowiedz)
        model_jwt = self._jwt_schemat.load(odpowiedz[0]).dostepowy
        self._jwt_opiekun.zapisz_jwt(model_jwt)

    def zarejestruj(self, model_uzytkownika: ModelUzytkownika) -> None or Blad:
        odpowiedz = self.i_klient_http.post("jwt", self._uzytkownik_schemat.dumps(model_uzytkownika),
                                            REJESTRACJA_ENDPOINT)
        if odpowiedz_kod := odpowiedz[1] != 200:
            return Blad(odpowiedz_kod, odpowiedz[0])

    def wyswietl_profil(self) -> ModelUzytkownika or Blad:
        odpowiedz = self.i_klient_http.get(url=PROFIL_ENDPOINT)
        if odpowiedz_kod := odpowiedz[1] != 200:
            return Blad(odpowiedz_kod, odpowiedz[0])
        return self._uzytkownik_schemat.load(odpowiedz[0])

from http_klient.I_klient_http import IKlientHttp
from http_klient.api.api_stale import LOGOWANIE_ENDPOINT, REJESTRACJA_ENDPOINT, PROFIL_ENDPOINT
from modele.uzytkownik.model_jwt import ModelJWT, JWTSchemat
from modele.uzytkownik.model_uzytkownika import ModelUzytkownika, UzytkownikSchemat
from przypadki_uzycia.blad import Blad


class FasadaUzytkownika:
    def __init__(self, i_klient_http: IKlientHttp):
        self.i_klient_http = i_klient_http
        self.uzytkownik_schemat = UzytkownikSchemat()
        self.jwt_schemat = JWTSchemat()

    def zaloguj(self, model_uzytkownika: ModelUzytkownika) -> ModelJWT or Blad:
        odpowiedz = self.i_klient_http.post(jwt="jwt", body=self.uzytkownik_schemat.dumps(model_uzytkownika),
                                            url=LOGOWANIE_ENDPOINT)
        # TODO: Zrobic response jako obiekt nie jako tupla
        if odpowiedz_kod := odpowiedz[1] != 200:
            return Blad(odpowiedz_kod, odpowiedz[0])
        return self.jwt_schemat.loads(odpowiedz[0])

    def zarejestruj(self, model_uzytkownika: ModelUzytkownika) -> None or Blad:
        odpowiedz = self.i_klient_http.post("jwt", self.uzytkownik_schemat.dumps(model_uzytkownika),
                                            REJESTRACJA_ENDPOINT)
        if odpowiedz_kod := odpowiedz[1] != 200:
            return Blad(odpowiedz_kod, odpowiedz[0])
        return None

    def wyswietl_profil(self) -> ModelUzytkownika or Blad:
        odpowiedz = self.i_klient_http.post(jwt="jwt", url=PROFIL_ENDPOINT)
        if odpowiedz_kod := odpowiedz[1] != 200:
            return Blad(odpowiedz_kod, odpowiedz[0])
        return self.uzytkownik_schemat.loads(odpowiedz[0])

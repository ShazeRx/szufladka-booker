from http_klient.I_klient_http import IKlientHttp
from http_klient.api.api_stale import LOGOWANIE_ENDPOINT,REJESTRACJA_ENDPOINT
from modele.uzytkownik.model_jwt import ModelJWT
from modele.uzytkownik.model_uzytkownika import ModelUzytkownika
from przypadki_uzycia.blad import Blad


class FasadaUzytkownika:
    def __init__(self, i_klient_http: IKlientHttp):
        self.i_klient_http = i_klient_http

    def zaloguj(self, model_uzytkownika: ModelUzytkownika) -> ModelJWT or Blad:
        return self.i_klient_http.post("jwt", model_uzytkownika.na_json(), LOGOWANIE_ENDPOINT)

    def zarejestruj(self,model_uzytkownika: ModelUzytkownika) -> None or Blad:
        return self.i_klient_http.post("jwt", model_uzytkownika.na_json(), REJESTRACJA_ENDPOINT)


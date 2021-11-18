import json
from unittest.mock import Mock

import pytest

from fasady.uzytkownicy.fasada_uzytkownika import FasadaUzytkownika
from http_klient.klient_http import KlientHttp
from modele.uzytkownik.model_jwt import ModelJWT, JWTSchemat
from modele.uzytkownik.model_uzytkownika import ModelUzytkownika, UzytkownikSchemat
from przypadki_uzycia.blad import Blad


class TestFasadaUzytkownika:

    @pytest.fixture
    def modelJWT(self):
        return ModelJWT("dostepowy", "odswiezajacy")

    @pytest.fixture
    def http_klient(self):
        mock = Mock(spec=KlientHttp)
        return mock

    @pytest.fixture
    def blad_json(self):
        return json.dumps({
            "message": "error"
        })

    @pytest.fixture
    def fasada_uzytkownika(self, http_klient):
        return FasadaUzytkownika(http_klient)

    @pytest.fixture
    def uzytkownik(self):
        return ModelUzytkownika(kryptonim="imie", haslo="haslo", email="email")

    def test_logowanie_powinien_zwrocic_model_jwt(self, http_klient, modelJWT, fasada_uzytkownika, uzytkownik):
        # zaloz
        jwt_json = JWTSchemat().dumps(modelJWT)
        http_klient.post.return_value = (jwt_json, 200)

        # dzialaj
        wynik = fasada_uzytkownika.zaloguj(model_uzytkownika=uzytkownik)

        # zapewnij
        http_klient.post.assert_called_once()
        assert wynik == modelJWT

    def test_logowanie_powinien_zwrocic_blad_przy_kodzie_innym_niz_200(self, http_klient, fasada_uzytkownika,
                                                                       uzytkownik, blad_json):
        # zaloz
        http_klient.post.return_value = (blad_json, 500)

        # dzialaj
        wynik = fasada_uzytkownika.zaloguj(model_uzytkownika=uzytkownik)

        # zapewnij
        http_klient.post.assert_called_once()
        assert isinstance(wynik, Blad)

    def test_rejestracja_powinien_zwrocic_nic(self, http_klient, fasada_uzytkownika, uzytkownik):
        # zaloz
        http_klient.post.return_value = (json.dumps({}), 200)

        # dzialaj
        wynik = fasada_uzytkownika.zarejestruj(model_uzytkownika=uzytkownik)

        # zapewnij
        http_klient.post.assert_called_once()
        assert wynik == None

    def test_rejestracja_powinien_zwrocic_blad_przy_kodzie_innym_niz_200(self, http_klient, fasada_uzytkownika,
                                                                         uzytkownik, blad_json):
        # zaloz
        http_klient.post.return_value = (blad_json, 500)

        # dzialaj
        wynik = fasada_uzytkownika.zarejestruj(model_uzytkownika=uzytkownik)

        # zapewnij
        http_klient.post.assert_called_once()
        assert isinstance(wynik, Blad)

    def test_profil_powienien_zwrocic_model_uzytkownika(self, http_klient, fasada_uzytkownika, uzytkownik):
        # zaloz
        uzytkownik_json = UzytkownikSchemat().dumps(uzytkownik)
        http_klient.post.return_value = (uzytkownik_json, 200)

        # dzialaj
        wynik = fasada_uzytkownika.wyswietl_profil()

        # zapewnij
        http_klient.post.assert_called_once()
        assert wynik == uzytkownik

    def test_profil_powinien_zwrocic_blad_przy_kodzie_innym_niz_200(self, http_klient, fasada_uzytkownika,
                                                                    blad_json):
        # zaloz
        http_klient.post.return_value = (blad_json, 500)

        # dzialaj
        wynik = fasada_uzytkownika.wyswietl_profil()

        # zapewnij
        http_klient.post.assert_called_once()
        assert isinstance(wynik, Blad)

import json
from unittest.mock import Mock

import pytest

from fasady.fasada_ksiazek.fasada_ksiazki import FasadaKsiazki
from http_klient.klient_http import KlientHttp
from modele.ksiazka.model_ksiazka import ModelKsiazki, KsiazkaSchemat
from przypadki_uzycia.blad import Blad


class TestFasadaKsiazki:
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
    def ksiazki(self):
        return [ModelKsiazki("Why we sleep", "Matthew Walker", 2017, "Helion"),
                ModelKsiazki("Why we sleep", "Matthew Walker", 2016, "Helion")]

    @pytest.fixture
    def fasada_ksiazki(self, http_klient):
        return FasadaKsiazki(http_klient)

    def test_powinien_oddac_ksiazke(self, fasada_ksiazki, http_klient):
        # zaloz
        http_klient.patch.return_value = (json.dumps({}), 200)

        # dzialaj
        wynik = fasada_ksiazki.oddaj_ksiazke()

        # zapewnij
        http_klient.patch.assert_called_once()
        assert wynik is None

    def test_powinien_zwrocic_blad_przy_oddawaniu(self, fasada_ksiazki, http_klient, blad_json):
        # zaloz
        http_klient.patch.return_value = (blad_json, 500)

        # dzialaj
        wynik = fasada_ksiazki.oddaj_ksiazke()

        # zapewnij
        http_klient.patch.assert_called_once()
        assert isinstance(wynik, Blad)

    def test_powinien_zwrocic_ksiazki_w_szufladce(self, fasada_ksiazki, http_klient, ksiazki):
        # zaloz
        ksiazki_json = KsiazkaSchemat().dumps(ksiazki, many=True)
        http_klient.get.return_value = (ksiazki_json, 200)

        # dzialaj
        wynik = fasada_ksiazki.pokaz_ksiazki_w_szufladce()

        # zapewnij
        http_klient.get.assert_called_once()
        assert wynik == ksiazki

    def test_powinien_zwrocic_blad_przy_pokazywaniu_ksiazek_w_szufladce(self, http_klient, blad_json, fasada_ksiazki):
        # zaloz
        http_klient.get.return_value = (blad_json, 500)

        # dzialaj
        wynik = fasada_ksiazki.pokaz_ksiazki_w_szufladce()

        # zapewnij
        http_klient.get.assert_called_once()
        assert isinstance(wynik, Blad)

    def test_powinien_pokazac_moje_ksiazki(self, http_klient, fasada_ksiazki, ksiazki):
        # zaloz
        ksiazki_json = KsiazkaSchemat().dumps(ksiazki, many=True)
        http_klient.get.return_value = (ksiazki_json, 200)

        # dzialaj
        wynik = fasada_ksiazki.pokaz_moje_ksiazki()

        # zapewnij
        http_klient.get.assert_called_once()
        assert wynik == ksiazki

    def test_powienien_zwrocic_blad_przy_pokazywaniu_moich_ksiazek(self, http_klient, fasada_ksiazki, blad_json):
        # zaloz
        http_klient.get.return_value = (blad_json, 500)

        # dzialaj
        wynik = fasada_ksiazki.pokaz_moje_ksiazki()

        # zapewnij
        http_klient.get.assert_called_once()
        assert isinstance(wynik, Blad)

    def test_powinien_dodac_ksiazke(self, http_klient, fasada_ksiazki):
        # zaloz
        ksiazka = ModelKsiazki("Why we sleep", "Matthew Walker", 2017, "Helion")
        ksiazka_json = KsiazkaSchemat().dumps(ksiazka, many=False)
        http_klient.post.return_value = (None, 200)

        # dzialaj
        wynik = fasada_ksiazki.dodaj_ksiazke()

        # zapewnij
        http_klient.post.assert_called_once()
        assert wynik is None

    def test_powinien_zwrocic_blad_przy_pokazywaniu_dodawaniu(self, http_klient, fasada_ksiazki, blad_json):
        # zaloz
        http_klient.post.return_value = (blad_json, 500)

        # dzialaj
        wynik = fasada_ksiazki.dodaj_ksiazke()

        # zapewnij
        http_klient.post.assert_called_once()
        assert isinstance(wynik, Blad)

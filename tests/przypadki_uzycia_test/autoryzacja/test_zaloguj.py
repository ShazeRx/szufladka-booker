from unittest.mock import Mock

import pytest

from fasady.uzytkownicy.fasada_uzytkownika import FasadaUzytkownika
from modele.uzytkownik.model_jwt import ModelJWT
from modele.uzytkownik.model_uzytkownika import ModelUzytkownika
from przypadki_uzycia.autoryzacja.zaloguj import ZalogujPrzypadekUzycia
from przypadki_uzycia.blad import Blad


class TestZaloguj:

    @pytest.fixture
    def modelJWT(self):
        return ModelJWT("dostepowy", "odswiezajacy")

    @pytest.fixture
    def mock_fasada(self, modelJWT):
        mock = Mock(spec=FasadaUzytkownika)
        return mock

    @pytest.fixture
    def uzytkownik(self):
        return ModelUzytkownika(kryptonim="imie", email="email@example.com", haslo="haslo")

    @pytest.fixture
    def przypadek_uzycia(self, mock_fasada):
        return ZalogujPrzypadekUzycia(mock_fasada)

    def test_powinien_zwrocic_model(self, przypadek_uzycia, uzytkownik, modelJWT, mock_fasada):
        # zaloz
        mock_fasada.zaloguj.return_value = modelJWT

        # dzialaj
        wynik = przypadek_uzycia.wykonaj(uzytkownik)

        # zapewnij
        assert wynik == modelJWT

    def test_powinien_zwrocic_blad(self, przypadek_uzycia, uzytkownik, mock_fasada):
        # zaloz
        mock_fasada.zaloguj.return_value = Blad(kod=300, wiadomosc="error")

        # dzialaj
        wynik = przypadek_uzycia.wykonaj(uzytkownik)

        # zapewnij
        assert isinstance(wynik, Blad)

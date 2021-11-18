import pytest
from unittest.mock import Mock

from fasady.uzytkownicy.fasada_uzytkownika import FasadaUzytkownika
from modele.uzytkownik.model_uzytkownika import ModelUzytkownika
from przypadki_uzycia.autoryzacja.zarejestruj import ZarejestrujPrzypadekUzycia
from przypadki_uzycia.blad import Blad


class TestZarejestruj:


    @pytest.fixture
    def mock_fasada(self):
        mock = Mock(spec=FasadaUzytkownika)
        return mock

    @pytest.fixture
    def uzytkownik(self):
        return ModelUzytkownika(kryptonim="imie",  email="email@example.com", haslo="haslo")

    @pytest.fixture
    def przypadek_uzycia(self, mock_fasada):
        return ZarejestrujPrzypadekUzycia(mock_fasada)

    def test_powinien_zwrocic_none(self, przypadek_uzycia, uzytkownik, mock_fasada):
        # zaloz
        mock_fasada.zarejestruj.return_value = None

        # dzialaj
        wynik = przypadek_uzycia.wykonaj(uzytkownik)

        # zapewnij
        assert wynik is None

    def test_powinien_zwrocic_blad(self, przypadek_uzycia, uzytkownik, mock_fasada):
        # zaloz
        mock_fasada.zarejestruj.return_value = Blad()

        # dzialaj
        wynik = przypadek_uzycia.wykonaj(uzytkownik)

        # zapewnij
        assert isinstance(wynik, Blad)

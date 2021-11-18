import json

import pytest

from modele.uzytkownik.model_uzytkownika import ModelUzytkownika


class TestModelUzytkownik:

    @pytest.fixture
    def uzytkownik(self):
        return ModelUzytkownika(kryptonim="buzz", haslo="email@example.com")

    @pytest.fixture
    def json(self):
        return json.dumps(dict(kryptonim='buzz', haslo='email@example.com'))

    def tests_powinien_utworzyc_model_usera_z_jsona(self, uzytkownik, json):
        # dzialaj
        model_uzytkownika = ModelUzytkownika.z_jsona(json)

        # zapewnij
        assert model_uzytkownika == uzytkownik

    def tests_powinien_utworzyc_jsona_z_uzytkownika(self, uzytkownik, json):
        # dzialaj
        uzytkownik_json = uzytkownik.na_json()

        # zapewnij
        assert uzytkownik_json == json

    def tests_powinien_zwrocic_jsona_z_emailem(self):
        # zaloz
        uzytkownik = ModelUzytkownika(kryptonim="buzz", haslo="haslo", email="email@example.com")

        # dzialaj
        uzytkownik_json = uzytkownik.na_json()

        # zapewnij
        assert 'haslo' in uzytkownik_json

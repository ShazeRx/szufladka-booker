import json

import pytest

from modele.uzytkownik.model_uzytkownika import ModelUzytkownika, UzytkownikSchemat


class TestModelUzytkownik:

    @pytest.fixture
    def uzytkownik(self):
        return ModelUzytkownika(kryptonim="buzz", haslo="email@example.com")

    @pytest.fixture
    def uzytkownik_json(self):
        return json.dumps(dict(kryptonim='buzz', haslo='email@example.com'))

    def tests_powinien_utworzyc_model_usera_z_jsona(self, uzytkownik, uzytkownik_json):
        # dzialaj
        model_uzytkownika = UzytkownikSchemat().loads(uzytkownik_json)

        # zapewnij
        assert model_uzytkownika == uzytkownik

    def tests_powinien_utworzyc_jsona_z_uzytkownika(self, uzytkownik, uzytkownik_json):
        # dzialaj
        uzytkownik_json = UzytkownikSchemat().dumps(uzytkownik)

        # zapewnij
        assert uzytkownik_json == uzytkownik_json

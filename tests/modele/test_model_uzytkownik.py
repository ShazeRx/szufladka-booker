import json

import pytest

from modele.uzytkownik.model_uzytkownika import ModelUzytkownika


class TestModelUzytkownik:

    @pytest.fixture
    def uzytkownik(self):
        return ModelUzytkownika("buzz", "oldrin", "email@example.com")

    @pytest.fixture
    def json(self):
        return json.dumps(dict(imie='buzz', nazwisko='oldrin', email='email@example.com'))

    def tests_powinien_utworzyc_model_usera_z_jsona(self, uzytkownik, json):
        # dzialaj
        model_uzytkownika = ModelUzytkownika.z_jsona(json)

        # zapewnij
        assert model_uzytkownika == uzytkownik

    def tests_powinien_utworzyc_jsona_z_uzytkownika(self, uzytkownik, json):
        # dzialaj
        uzytkownikJson = uzytkownik.na_json()

        # zapewnij
        assert uzytkownikJson == json

    def tests_powinien_zwrocic_jsona_z_haslem(self):
        # zaloz
        uzytkownik = ModelUzytkownika("buzz", "oldrin", "email@example.com", haslo="haslo")

        # dzialaj
        uzytkownikJson = uzytkownik.na_json()

        # zapewnij
        assert 'haslo' in uzytkownikJson

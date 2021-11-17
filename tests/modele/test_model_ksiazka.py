import json

import pytest

from modele.ksiazka.model_ksiazka import ModelKsiazki


class TestModelKsiazki:

    @pytest.fixture
    def ksiazka(self):
        return ModelKsiazki("Why we sleep", "Matthew Walker", 2017, "Helion")

    @pytest.fixture
    def json(self):
        return json.dumps(dict(tytul='Why we sleep', autor='Matthew Walker', rok_wydania=2017, wydawnictwo='Helion'))

    def tests_powinien_utworzyc_model_ksiazki_z_jsona(self, ksiazka, json):
        # dzialaj
        model_ksiazki = ModelKsiazki.z_jsona(json)

        # zapewni
        assert model_ksiazki == ksiazka

    def tests_powinien_utworzyc_jsona_z_ksiazki(self, ksiazka, json):
        # dzialaj
        ksiazka_json = ksiazka.na_json()

        # zapewni
        assert ksiazka_json == json


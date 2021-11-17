from __future__ import annotations
from dataclasses import dataclass

from modele.mieszanki.json_serializacyjny_mieszanka import JsonSerializacyjnyMieszanka


@dataclass
class ModelUzytkownika(JsonSerializacyjnyMieszanka):
    def __init__(self, imie: str, nazwisko: str, email: str, **kwargs):
        super().__init__(imie=imie, nazwisko=nazwisko, email=email, **kwargs)

    @property
    def daj_imie(self):
        return self._imie

    @property
    def daj_nazwisko(self):
        return self._nazwisko

    @property
    def daj_email(self):
        return self._email

    def ustaw_haslo(self, haslo: str) -> None:
        self._haslo = haslo

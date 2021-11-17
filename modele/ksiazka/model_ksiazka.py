from dataclasses import dataclass

from modele.mieszanki.json_serializacyjny_mieszanka import JsonSerializacyjnyMieszanka


@dataclass
class ModelKsiazki(JsonSerializacyjnyMieszanka):
    def __init__(self, tytul, autor, rok_wydania, wydawnictwo):
        super().__init__(tytul=tytul, autor=autor, rok_wydania=rok_wydania, wydawnictwo=wydawnictwo)

    def daj_tytul(self) -> str:
        return self._tytul

    def ustaw_tytul(self, tytul: str) -> None:
        self._tytul = tytul

    def daj_autor(self) -> str:
        return self._autor

    def ustaw_autor(self, autor: str) -> None:
        self._autor = autor

    def daj_rok_wydania(self) -> int:
        return self._rok_wydania

    def ustaw_rok_wydania(self, rok_wydania: int) -> None:
        self._rok_wydania = rok_wydania

    def daj_wydawnictwo(self) -> str:
        return self._wydawnictwo

    def ustaw_wydawnictwo(self, wydawnictwo: str) -> None:
        self._wydawnictwo = wydawnictwo

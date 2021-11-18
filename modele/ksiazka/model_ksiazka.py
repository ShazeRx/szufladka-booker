from dataclasses import dataclass

from modele.mieszanki.json_serializacyjny_mieszanka import JsonSerializacyjnyMieszanka


@dataclass
class ModelKsiazki(JsonSerializacyjnyMieszanka):
    def __init__(self, tytul, autor, rok_wydania, wydawnictwo):
        super().__init__(tytul=tytul, autor=autor, rok_wydania=rok_wydania, wydawnictwo=wydawnictwo)

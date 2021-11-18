from __future__ import annotations
from dataclasses import dataclass

from modele.mieszanki.json_serializacyjny_mieszanka import JsonSerializacyjnyMieszanka


@dataclass
class ModelUzytkownika(JsonSerializacyjnyMieszanka):
    def __init__(self, kryptonim=None, haslo=None,**kwargs):
        super().__init__(kryptonim=kryptonim, haslo=haslo,**kwargs)

from __future__ import annotations

import json


class JsonSerializacyjnyMieszanka:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __eq__(self, other):
        return self._jako_slownik() == other.__dict__

    def _jako_slownik(self):
        return {k.removeprefix("_"): val for k, val in self.__dict__.items()}

    def na_json(self) -> str:
        return json.dumps(self._jako_slownik())

    @staticmethod
    def z_jsona(json_slowo: str):
        return JsonSerializacyjnyMieszanka(**json.loads(json_slowo))

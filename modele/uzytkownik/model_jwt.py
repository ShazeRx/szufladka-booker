from modele.mieszanki.json_serializacyjny_mieszanka import JsonSerializacyjnyMieszanka


class ModelJWT(JsonSerializacyjnyMieszanka):
    def __init__(self, dostepowy: str, odswiezajacy: str):
        super().__init__(dostepowy=dostepowy, odswiezajacy=odswiezajacy)

    @property
    def daj_dostepowy(self):
        return self._dostepowy

    @property
    def daj_odswiezajacy(self):
        return self._odswiezajacy

from dataclasses import dataclass

from marshmallow import Schema, fields, post_load


@dataclass
class ModelKsiazki:
    def __init__(self, indeks, tytul, autor, rok_wydania, wydawnictwo):
        self.indeks = indeks
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania
        self.wydawnictwo = wydawnictwo


class KsiazkaSchemat(Schema):
    indeks = fields.Integer()
    tytul = fields.Str()
    autor = fields.Str()
    rok_wydania = fields.Integer()
    wydawnictwo = fields.Str()

    @post_load
    def make_object(self, data, **kwargs):
        return ModelKsiazki(**data)

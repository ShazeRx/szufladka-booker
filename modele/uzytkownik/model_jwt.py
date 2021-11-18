from dataclasses import dataclass

from marshmallow import Schema, fields, post_load


@dataclass
class ModelJWT:
    def __init__(self, dostepowy: str, odswiezajacy: str):
        self.dostepowy = dostepowy
        self.odswiezajacy = odswiezajacy


class JWTSchemat(Schema):
    odswiezajacy = fields.Str()
    dostepowy = fields.Str()

    @post_load
    def make_object(self, data, **kwargs):
        return ModelJWT(**data)

from __future__ import annotations

from dataclasses import dataclass

from marshmallow import Schema, fields, post_load


@dataclass
class ModelUzytkownika:
    def __init__(self, id=None, kryptonim=None, haslo=None, email=None):
        self.id = id
        self.kryptonim = kryptonim
        self.haslo = haslo
        self.email = email


class UzytkownikSchemat(Schema):
    id = fields.Integer()
    kryptonim = fields.Str()
    email = fields.Str(required=False)
    haslo = fields.Str()

    @post_load
    def make_object(self, data, **kwargs):
        return ModelUzytkownika(**data)

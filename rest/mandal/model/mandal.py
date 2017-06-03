import copy
from datetime import datetime

from voluptuous import Schema, Length, All, Required, Inclusive, PREVENT_EXTRA

from ganeshutsav_rest.rest.common.model.db import DbObject


class Mandal(DbObject):
    schema = Schema({
        Required('name')           : All(str, Length(min=1)),
        'location'                 : All(Schema({
            Inclusive('lat', 'latlong') : float,
            Inclusive('long', 'latlong'): float,
        })),
        'date_established'         : datetime,
        Required('primary_contact'): str

    }, extra=PREVENT_EXTRA)

    def __init__(self):
        self._collection = 'mandal'
        self._fields = {}
        self._init_db_object()

    @classmethod
    def init_using_params(cls, data):
        instance = cls()
        instance.load(data)
        return instance

    @classmethod
    def init_empty_object(cls):
        return cls()

    def load(self, d):
        self._fields = Mandal.schema(d)

        # def __setattr__(self, key, value):
        #     original_fields = copy.deepcopy(self._fields)
        #     original_fields[key] = value
        #     new_fields = Mandal.schema(original_fields)
        #     self._fields = new_fields
        #
        # def __getattr__(self, item):
        #     fields = self.__dict__['_fields']
        #     if item in fields:
        #         return fields[item]
        #     else:
        #         raise AttributeError('Attribute not found: {0}'.format(item))

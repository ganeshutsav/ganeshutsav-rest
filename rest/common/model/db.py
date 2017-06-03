from pymongo import MongoClient


class DbObject(object):
    """
    Inheriting classes should have the following attributes for this to work properly.
    _fields which stores the atrributes that will be saved/retrieved from database
    _collection which stores the collection to work on

    """

    def _init_db_object(self):
        self._collection = MongoClient().get_database('ganeshutsav').get_collection(self._collection)

    def save(self):
        result = self._collection.insert_one(self._fields)
        if result.acknowledged:
            return result.inserted_id
        else:
            raise Exception('Failed to insert document')

    def list_all(self):
        # FIXME Remove this
        result = list(self._collection.find({}))
        for item in result:
            item.pop('_id', None)
        return result

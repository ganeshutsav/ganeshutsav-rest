"""
dbsetup.py
"""
import logging
import pymongo
import sys
import yaml

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
log = logging.getLogger(__name__)

if __name__ == '__main__':
    config = yaml.load(open('config.yaml', 'r')).get('database')

    db = pymongo.MongoClient().get_database(config['db_name'])
    collections = config['collections']

    for collection in collections:
        log.info('Recreating collection: {0}'.format(collection))
        db.drop_collection(collection)
        db.create_collection(collection)
        
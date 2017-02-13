import pymongo
from pymongo import MongoClient

from config import Config

app = Config
app.set_env(app, 'dev')
conf = app.conf

client = MongoClient('mongodb://' + conf['MONGO_HOST'] + ':' + conf['MONGO_PORT'])
db = client.fschk_db
scans = db.fschk_scans


def insert_scan_result(scan):
    scans = db.fschk_scans
    scans.insert_one(scan)


def get_scan_result(filters={}):
    if not filters:
        scan = scans.find_one()
    else:
        scan = scans.find_one(filters)
    return scan


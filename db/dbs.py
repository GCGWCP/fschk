#!/usr/bin/env python

from sqlalchemy import create_engine, MetaData
from sqlalchemy.sql import select
from sqlalchemy.ext.declarative import declarative_base
from db import db_models
from config import Config


app = Config
app.set_env(app, 'dev')
conf = app.conf


def connect(user, password, db, host='localhost', port=5432):
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)
    con = create_engine(url, client_encoding='utf8')
    meta = MetaData(bind=con, reflect=True)
    return con, meta


def fschk_connect():
    return connect(
        conf['PG_USER'],
        conf['PG_PWORD'],
        conf['PG_DB'],
        conf['PG_HOST'],
        conf['PG_PORT']
    )


def table_exists(model):
    con, meta = fschk_connect()

    Base = declarative_base()

    class TemporaryModel(model, Base):
        __tablename__ = model.__tablename__

    if Base.metadata.tables:
        return True
    else:
        return False


def table_count():
    con, meta = fschk_connect()

    count = len(meta.tables)
    return count


def create_table(model):
    con, meta = fschk_connect()

    Base = declarative_base()

    class TemporaryModel(model, Base):
        __tablename__ = model.__tablename__

    Base.metadata.create_all(bind=con)


def instantiate_db():
    try:
        create_table(db_models.File)
        # create_table(db_models.FileSystem)
        # create_table(db_models.OS)
        # create_table(db_models.Process)
        # create_table(db_models.Kmod)
        # create_table(db_models.Node)
        # create_table(db_models.Device)
        # create_table(db_models.TCPSYNPacketSignature)
        # create_table(db_models.DNSFingerPrint)
        # create_table(db_models.IPv4Address)
        # create_table(db_models.Connection)
    finally:
        print('Tables created')


def select_from(table, query=None):
    con, meta = fschk_connect()
    if query:
        result = con.execute(meta.tables[table].select(whereclause=query))
    else:
        result = con.execute(meta.tables[table].select())
    return result


def insert_row(table, columns={}):
    con, meta = fschk_connect()
    cols = columns
    con.execute(meta.tables[table].insert(), cols)


def insert_row_from_object(obj):
    table = obj.__tablename__
    con, meta = fschk_connect()
    cols = [obj.__dict__]
    con.execute(meta.tables[table].insert(), cols)


def insert_rows_from_objects(table, obj_set):
    con, meta = fschk_connect()
    cols = [obj.__dict__ for obj in obj_set]
    con.execute(meta.tables[table].insert(), cols)


def update_row(table, columns={}):
    con, meta = fschk_connect()
    # select -> insert


def db_is_instantiated():
    con, meta = fschk_connect()
    tables = [table for table in meta.tables]
    if tables != []:
        return True
    else:
        return False


def main():
    pass


if __name__ == '__main__':
    instantiate_db()

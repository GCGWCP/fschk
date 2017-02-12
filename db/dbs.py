#!/usr/bin/env python

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from models import File
from config import Config
Base = declarative_base()

app = Config()
app.set_env('dev')


def connect(user, password, db, host='localhost', port=5432):
    url = 'postgresql://{}:{}@{}:{}/{}'
    url.format(user, password, host, port, db)
    con = create_engine(url, client_encoding='utf8')
    meta = MetaData(bind=con, reflect=True)
    return con, meta


def select(table, column=[], value=[]):
    con, meta = connect(
        app.conf['POSTGRES_USER'],
        app.conf['POSTGRES_PWORD'],
        app.conf['POSTGRES_DB']
    )
    if not column:
        s = con.select([table])
        result = s.execute()
    elif column and not value:
        s = con.select([table.col for col in column])
        result = s.execute()
    elif column and value:
        s = con.select([table]).where(table.column == value)
        result = s.execute()

    con.close()
    return result


def insert_row(table, columns={}):
    con, meta = connect(
        app.conf['POSTGRES_USER'],
        app.conf['POSTGRES_PWORD'],
        app.conf['POSTGRES_DB']
    )
    cols = [columns]
    con.execute(meta.tables[table].insert(), cols)
    con.close()


def insert_rows(table, columns={}):
    con, meta = connect(
        app.conf['POSTGRES_USER'],
        app.conf['POSTGRES_PWORD'],
        app.conf['POSTGRES_DB']
    )
    cols = [columns]
    for col in cols:
        con.execute(meta.tables[table].insert(), col)
    con.close()


def update_row(table, columns={}):
    con, meta = connect(
        app.conf['POSTGRES_USER'],
        app.conf['POSTGRES_PWORD'],
        app.conf['POSTGRES_DB']
    )
    # select -> insert
    con.close()


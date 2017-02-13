#!/usr/bin/env python

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from db.db_models import File
from config import Config
Base = declarative_base()

app = Config
app.set_env(app, 'dev')
conf = app.conf


def connect(user, password, db, host='localhost', port=5432):
    # url = 'postgresql://' + user + ':' + password + '@' + host + ':' + port + '/' + db
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


def select(table=None, column=[], value=[]):
    con, meta = fschk_connect()
    if not column:
        s = meta.tables[table]
        result = s.execute()
        print(result)
    elif column and not value:
        s = meta.tables[table]
        result = s.execute()
    elif column and value:
        s = meta.tables[table]
        result = s.execute()

    con.close()
    return result


def insert_row(table, columns={}):
    con, meta = fschk_connect()
    cols = [columns]
    con.execute(meta.tables[table].insert(), cols)
    con.close()


def insert_rows(table, columns={}):
    con, meta = fschk_connect()
    cols = [columns]
    for col in cols:
        con.execute(meta.tables[table].insert(), col)
    con.close()


def update_row(table, columns={}):
    con, meta = fschk_connect()
    # select -> insert
    con.close()


def db_is_instantiated():
    try:
        select()
        return False
    except KeyError:
        return True


def main():
    pass


if __name__ == '__main__':
    main()

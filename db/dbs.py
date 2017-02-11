#!/usr/bin/env python

from config import app

from sqlalchemy import create_engine
engine = create_engine('postgresql://scott:tiger@localhost:5432/mydatabase')


def create_db():
    pass


def init_tables():
    pass


def connect_to_pgsql():
    pass


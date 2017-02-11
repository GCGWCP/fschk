#!/usr/bin/env python

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref
Base = declarative_base()
engine = create_engine('postgresql://schroder@localhost:5432/fschk')


class File(Base):
    __tablename__ = 'Files'

    id = Column(Integer, primary_key=True)
    file_name = Column(String, nullable=True)
    root_path = Column(String, nullable=True)
    size = Column(Integer, nullable=True)
    permissions = Column(Integer, nullable=True)
    created = Column(DateTime, nullable=True)
    last_modified = Column(DateTime, nullable=True)
    last_accessed = Column(DateTime, nullable=True)
    owner = Column(Integer, nullable=True)
    group = Column(Integer, nullable=True)
    inode = Column(Integer, nullable=True)
    file_type = Column(String, nullable=True)
    ext_attr = Column(String, nullable=True)
    sticky_bit = Column(Integer, nullable=True)
    encoding = Column(String, nullable=True)
    sha256 = Column(String, nullable=True)
    sha512 = Column(String, nullable=True)

def create_table():
    


def init_tables():
    pass




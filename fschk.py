#!/usr/bin/env python3

"""
    0) Create databases of file info.
    1) Iterate through designated branches of fs.
    2) Create hashes of various file info.
    3) Check against databases.
    4) Output results.
"""

import sys


from utils.fsnav import *
from db.dbs import *


def is_first_run():
    if db_is_instantiated():
        return False
    else:
        return True


def first_run():
    create_db()


def daemon():
    pass


def main():
    if is_first_run():
        print('Is first run:')
        instantiate_db()
    else:
        gen = traverse_gen('.')
        while True:
            try:
                fname = next(gen)
                try:
                    write_obj_to_db(finfo(fname))
                except FileNotFoundError:
                    pass

            except StopIteration:
                sys.exit(1)


if __name__ == '__main__':
    main()

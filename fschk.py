#!/usr/bin/env python3

"""
    0) Create database of file info.
    1) Iterate through designated branches of fs.
    2) Create table in database for scan.
    3) Collect various file info and create hashes.
    4) Check table against past tables to create diff.
    5) Output results.
"""

import sys

from utils.fsnav import *
from db.dbs import *
from db.db_models import File


def daemon():
    pass


def main():
    if is_first_run():
        print('Is first run:')
        instantiate_db()
        current_table = 'files_0'
        scan_and_store('.', current_table)
        sys.exit(1)
    else:
        current_table = create_seq_table(File)
        scan_and_store('.', current_table)
        sys.exit(1)


if __name__ == '__main__':
    main()

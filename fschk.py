#!/usr/bin/env python3

"""
    0) Create databases of file info.
    1) Iterate through designated branches of fs.
    2) Create hashes of various file info.
    3) Check against databases.
    4) Output results.
"""

import os
import sys
import hashlib
import optparse


from utils import fsnav
from db.dbs import *


# With thanks to Omnifarious
# https://stackoverflow.com/questions/3431825/generating-an-md5-checksum-of-a-file
def hash_bytestr_iter(bytesiter, hasher, ashexstr=False):
    for block in bytesiter:
        hasher.update(block)
    return (hasher.hexdigest() if ashexstr else hasher.digest())


def file_as_blockiter(afile, blocksize=65536):
    with afile:
        block = afile.read(blocksize)
        while len(block) > 0:
            yield block
            block = afile.read(blocksize)


def is_first_run():
    pass


def first_run():
    create_db()
    init_tables()


def daemon():
    pass


def main():
    gen = fsnav.traverse_gen('.')
    while True:
        try:
            fname = next(gen)
            try:
                fsnav.finfo(fname)

                with open(fname, 'rb') as f:
                    shasum = hash_bytestr_iter(file_as_blockiter(f), hashlib.sha256(), ashexstr=True)
                    print('File SHA256:', shasum)
                    print()

            except FileNotFoundError:
                pass

        except StopIteration:
            sys.exit(1)


if __name__ == '__main__':
    main()

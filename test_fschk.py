#!/usr/bin/env python

import unittest
import subprocess
import os
from itertools import combinations as combs
from itertools import combinations_with_replacement as combs_wr
from itertools import product as xprod
from itertools import permutations as perms
from models import *
from db import *



class TestException(Exception):
    pass


class TestFileInfo(unittest.TestCase):
    def setUp(self):
        self.test_root_dir = os.path.join(os.getcwd(), 'test_dir')
        subprocess.call(['mkdir', self.test_root_dir])

        # Create a handful of directories with fucked up names to travese.
        self.test_dirs_first_branch = [
            'test1',
            '.test2',
            '/test3',
            '\0test',
            'test; yes',
            ':test:'
        ]

        # Create a bunch of file names to create in our directories.
        self.test_file_names = [
            [
                ''.join(
                    [str(i) for i in comb]
                ) for comb in combs([1, 2, 3, 4, 'a', 'b', 'c', 'd'], 3)
            ]
        ]


    def tearDown(self):
        # Delete dir and files for testing.
        subprocess.call(['rm', '-rf', self.test_root_dir])


if __name__ == '__main__':
    unittest.main()

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
from utils import fsnav


class TestException(Exception):
    pass


class TestFschk(unittest.TestCase):
    def setUp(self):
        # Establish the root to create the test directory.
        self.test_root_dir = os.path.join(os.getcwd(), 'test_dir')

        # Create a handful of directories with fucked up names to travese.
        self.test_dirs_first_branch = [
            'test1',
            '.test2'
            # '/test3',
            # '\0test',
            # 'test; yes',
            # ':test:'
        ]

        self.test_dirs_second_branch = [
            'dir1',
            '.dir2'
        ]

        # Create a bunch of file names to create in our directories.
        self.test_file_names = [
            ''.join(
                [str(i) for i in comb]
            ) for comb in combs([1, 2, 3, 'a', 'b', 'c'], 3)
        ]

        # Build test directory tree root.
        subprocess.call(['mkdir', self.test_root_dir])
        os.chdir(self.test_root_dir)

        # Populate the test directory with files.
        for name in self.test_file_names:
            subprocess.call(['touch', name])
        os.chdir('..')

        return self

    def test_traverse_dir(self):
        test_traverse_file_list = fsnav.traverse(self.test_root_dir)
        print(test_traverse_file_list)
        self.assertEqual(self.test_file_names, test_traverse_file_list)

    def test_finfo(self):
        self.assertEqual(1, 1)

    def tearDown(self):
        # Delete dir and files for testing.
        subprocess.call(['rm', '-rf', self.test_root_dir])


if __name__ == '__main__':
    unittest.main()

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
            [
                ''.join(
                    [str(i) for i in comb]
                ) for comb in combs([1, 2, 3, 'a', 'b', 'c'], 3)
            ]
        ]

        self.test_dirs_full_paths = []
        self.test_dirs_full_paths.append(
            [os.path.join(self.test_root_dir, test_dirs_first_branch)]
        )

        for test_dir in self.test_dirs_full_paths:
            for test_second_branch_dir in self.test_dirs_second_branch:
                self.test_dirs_full_paths.append(
                    [os.path.join(test_dir, test_second_branch_dir)]
                )

        # Build test directory tree.
        subprocess.call(['mkdir', self.test_root_dir])

        for test_dir in self.test_dirs_full_paths:
            subprocess.call(['mkdir', test_dir])

        # Populate test directories with files.
        for test_dir in self.test_dirs_full_paths:
            for test_file in test_file_names:
                subprocess.call(['touch', test_file])

    def test_traverse_dir(self):
        test_file_list = []
        test_traverse_file_list = travese(self.test_root_dir)
        assertEqual(test_file_list, test_traverse_file_list)

    def test_finfo(self):
        assertEqual(1,1)

    def tearDown(self):
        # Delete dir and files for testing.
        subprocess.call(['rm', '-rf', self.test_root_dir])


if __name__ == '__main__':
    unittest.main()

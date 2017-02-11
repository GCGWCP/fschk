#!/usr/bin/env python

import unittest
import subprocess
import os
from itertools import combinations as combs
from itertools import combinations_with_replacement as combs_wr
from itertools import product as xprod
from itertools import permutations as perms
from models import Directories, File
from db import *


class TestException(Exception):
    pass


class TestFileInfo(unittest.TestCase):
    def setUp(self):
        if os.getcwd() != os.path.join(env['ABS_PATH_TO_APP'], 'tests'):
            raise TestException('Start tests from ' + os.path.join(env['ABS_PATH_TO_APP'], 'tests') + 'because we are doing danger here.')

        subprocess.call(['mkdir', self.test_dir_root])

        # Create a handful of directories with fucked up names to travese.
        test_dirs_first_branch = [
            'test1',
            '.test2',
            '/test3',
            '\0test',
            'test; yes',
            ':test:'
        ]

        # Create a bunch of file names to create in our directories.
        test_file_names = [
            [
                ''.join(
                    [str(i) for i in comb]
                ) for comb in combs([1, 2, 3, 4, 'a', 'b', 'c', 'd'], 3)
            ]
        ]

        return [self.test_dir_root, test_dirs_first_branch, test_file_names]

    def test_in_test_dir(self):
        this_dir = os.getcwd()
        target_dir = os.path.realpath(__file__)
        self.assertEqual(target_dir, this_dir)

    @classmethod
    def tearDownClass(self):
        # Delete dir and files for testing.
        subprocess.call(['rm', '-rf', './test_dir'])


if __name__ == '__main__':
    unittest.main()

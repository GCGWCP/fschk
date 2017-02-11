#!/usr/bin/env python3


import os
import stat
import subprocess
import xattr
from chardet.universaldetector import UniversalDetector
from models import File


def traverse(target_dir):

        file_list = []
        for root, dirs, files in os.walk(target_dir, topdown=False):
            for name in files:
                file_list.append(name)
        return file_list


def traverse_generator(target_dir):
    # Write list of files to traverse to tmp_file(s)
    # Prevents loading huge list of files into memory.
    tmp_list = './tmp_list.txt'
    with open(tmp_list, 'w') as f:
        for root, dirs, files in os.walk(target_dir, topdown=False):
            for name in files:
                f.write(os.path.join(root, name) + '\n')

    # Get line count for generator loop without spending the generator
    # line_count = int(os.popen('wc -l ' + tmp_list).read().split()[0])

    # Generator from tmp_list of /paths/to/files to operate on
    with open(tmp_list, 'r') as f:
        for line in f:
            yield f.readline().strip('\n')
    return tmp_list


def traverse_generator_cleanup(target_dir):
    """
        Just want to get rid of the tmp file(s) created for
        the directory tree traversal with a separate function.
    """
    try:
        subprocess.call(['rm', '-f', target_dir])
    except IOError as err:
        print(err)


def detect_file_encoding(fname):
    # Heuristic, takes forever, run async
    detector = UniversalDetector()
    for line in open(fname, 'rb'):
        detector.feed(line)
        if detector.done:
            break
    detector.close()
    print(fname, 'File Encoding:', detector.result)
    return detector.result


def detect_mime_type(fname):
    pass


def finfo(fname):
    f = File
    info = os.stat(fname)
    print('File Name:', fname)
    name = fname.split('/')
    file_name = name[len(name) - 1]
    f.name = file_name
    print('File Name:', f.name)
    root_path = os.path.realpath(fname).split('/')
    f.root_path = '/'.join(root_path[0:len(root_path) - 1]) + '/'
    print('File Root Path:', f.root_path)
    f.size = info.st_size
    print('File Size:', f.size)
    f.permissions = oct(os.stat(fname).st_mode)[-3:]
    print('File Permissions:', f.permissions)
    f.inode = info.st_ino
    print('File Inode:', f.inode)
    f.owner = info.st_uid
    print('File Owner:', f.owner)
    f.group = info.st_gid
    print('File Group Owner:', f.group)
    f.last_modified = info.st_mtime
    print('File Last Modified:', f.last_modified)
    f.file_type = stat.S_IFMT(info.st_mode)
    print('File Type:', f.file_type)
    f.ext_attr = xattr.xattr(fname)
    print('File Extended Attributes', f.ext_attr.keys())
    return f


def main():
    pass


if __name__ == '__main__':
    main()

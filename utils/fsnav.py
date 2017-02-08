#!/usr/bin/env python3


import os
import stat
import xattr
from chardet.universaldetector import UniversalDetector
from models import File


def traverse(dir):
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            info = finfo(os.path.join(root, name))
            print(info)


def traverse_gen(dir):
    # Write list of files to traverse to tmp_file
    tmp_list = './tmp_list.txt'
    with open(tmp_list, 'w') as f:
        for root, dirs, files in os.walk(".", topdown=False):
            for name in files:
                f.write(os.path.join(root, name) + '\n')

    # Get line count for generator loop without spending the generator
    # line_count = int(os.popen('wc -l ' + tmp_list).read().split()[0])

    # Generator from tmp_list of /paths/to/files to operate on
    with open(tmp_list, 'r') as f:
        for line in f:
            yield f.readline().strip('\n')
        os.popen('rm ' + tmp_list)


def detect_file_encoding(fname):
    detector = UniversalDetector()
    for line in open(fname, 'rb'):
        detector.feed(line)
        if detector.done:
            break
    detector.close()
    return detector.result


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
    f.encoding = detect_file_encoding(fname)
    print('File Encoding:', f.encoding)
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

#!/usr/bin/env python3


import os
import stat
import xattr
from chardet.universaldetector import UniversalDetector


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
    os_info = os.stat(fname)
    print('File Name:', fname)
    encoding = detect_file_encoding(fname)
    print('File Encoding:', encoding)
    fsize = os_info.st_size
    print('File Size:', fsize)
    inode = os_info.st_ino
    print('File Inode:', inode)
    permissions = oct(os.stat(fname).st_mode)[-3:]
    print('File Permissions:', permissions)
    owner = os_info.st_uid
    print('File Owner:', owner)
    group = os_info.st_gid
    print('File Group Owner:', group)
    last_mod = os_info.st_mtime
    print('File Last Modified:', last_mod)
    file_type = stat.S_IFMT(os_info.st_mode)
    print('File Type:', file_type)
    ext_attr = xattr.xattr(fname)
    print('File Extended Attributes', ext_attr.keys())


def main():
    pass


if __name__ == '__main__':
    main()

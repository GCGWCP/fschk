#!/usr/bin/env python3

import os
import stat
import xattr
from chardet.universaldetector import UniversalDetector
from db import db_models, dbs
from utils import hash_utils


def is_first_run():
    if dbs.db_is_instantiated():
        return False
    else:
        if not os.path.exists('/var/log/fschk'):
            os.mkdir('/var/log/fschk')
        return True


def traverse(target_dir):
        file_list = []
        for root, dirs, files in os.walk(target_dir, topdown=False):
            for name in files:
                file_list.append(name)
        return file_list


def traverse_gen(target_dir):
    # Write list of files to traverse to tmp_file(s)
    # Prevents loading huge list of files into memory.
    tmp_list = '/var/log/fschk/tmp_list.txt'
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


def traverse_gen_cleanup():
    """
        Just want to get rid of the tmp file(s) created for
        the directory tree traversal with a separate function.
    """
    tmp_list = '/var/log/fschk/tmp_list.txt'
    try:
        tmp_file_list = open(tmp_list, 'r')
        tmp_file_list.close()
        os.remove(tmp_list)
        return 'tmp_list cleaned'
    except IOError as err:
        print(err)


def detect_file_encoding(fname):
    # Heuristic, takes forever, run async and insert into
    # existing entry.
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
    f = db_models.File()
    info = os.stat(fname)
    name = fname.split('/')
    file_name = name[len(name) - 1]
    f.file_name = file_name
    full_path = os.path.realpath(fname)
    f.full_path = full_path
    root_path = full_path.split('/')
    f.root_path = '/'.join(root_path[0:len(root_path) - 1]) + '/'
    f.size = info.st_size
    f.permissions = info.st_mode
    f.inode = info.st_ino
    f.owner = info.st_uid
    f.group = info.st_gid
    f.created = info.st_ctime
    f.last_modified = info.st_mtime
    f.last_accessed = info.st_atime
    f.file_type = stat.S_IFMT(info.st_mode)
    ext_attr = xattr.xattr(fname)
    if ext_attr.keys() == []:
        f.ext_attr = 'none'
    else:
        f.ext_attr = ','.join(ext_attr.keys())
    f.sticky_bit = bool(info.st_mode & 0o01000 == 512)
    f.encoding = 'Undetermined'
    f.sha256 = hash_utils.get_sha256(fname)
    f.sha512 = ''
    return f


def write_obj_to_db(f_obj, table):
    try:
        dbs.insert_row(table, f_obj.__dict__)
    finally:
        print('Wrote:\n', f_obj, 'to DB')


def scan_and_store(root_dir, table):
    gen = traverse_gen(root_dir)
    while True:
        try:
            fname = next(gen)
            try:
                write_obj_to_db(finfo(fname), table)
            except FileNotFoundError as err:
                print('Finished Scan.')
                pass
        except StopIteration:
            break
    traverse_gen_cleanup()


def main():
    pass


if __name__ == '__main__':
    main()

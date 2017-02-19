#!/usr/bin/env python


def changed_files(table1, table2):
    """
        select files_1.full_path, files_1.size, files_2.size
        from files_1
        inner join files_2
        on files_1.full_path = files_2.full_path
        and files_1.sha256 != files_2.sha256;
    """
    pass


def new_files(table1, table2):
    pass


def deleted_files(table1, table2):
    pass


def moved_files(table1, table2):
    pass


def main():
    pass


if __name__ == '__main__':
    main()

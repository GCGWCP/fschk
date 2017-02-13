import optparse


def parse_args():
    parser = optparse.OptionParser()
    parser.add_option(
        '-b',
        '--background-daemon',
        help='Run as background daemon'
    )
    parser.add_option(
        '-d',
        '--dir',
        action='append',
        type='string',
        default=[],
        metavar='/path/to/DIR',
        help='Base directories of directory trees to scan'
    )
    parser.add_option(
        '-i',
        '--interval',
        action='store',
        type='int',
        default='3600',
        help='Set interval to run scans in seconds'
    )
    parser.add_option(
        '-l',
        '--log-session',
        action='store_true',
        dest='logging_enabled',
        help='Log session'
    )
    parser.add_option(
        '-L',
        '--log-file',
        action='store',
        type='string',
        metavar='/path/to/LOGFILE.log',
        help='Set log file for session'
    )
    parser.add_option(
        '-q',
        '--quiet',
        action='store_const',
        const=0,
        dest='verbose'
    )
    parser.add_option(
        '-x',
        '--exclude-dir',
        action='append',
        type='string',
        default=[],
        metavar='/path/to/dir1 /path/to/dir2',
        help='Directories to exclude from scan'
    )
    parser.add_option(
        '-v',
        '--verbose',
        action='count',
        count=1,
        dest='verbose'
    )

    return parser


if __name__ == '__main__':
    parse_args()

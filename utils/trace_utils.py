#!/usr/bin/env python

import psutil
import socket
from ctypes import struct


def ip2int(addr):
    return struct.unpack("!I", socket.inet_aton(addr))[0]


def int2ip(addr):
    return socket.inet_ntoa(struct.pack("!I", addr))


def get_listening_conxns():
    conxns = psutil.net_connections()
    listening_conxns = [cx for cx in conxns if cx[5] == 'LISTEN']
    return listening_conxns


def get_established_conxns():
    conxns = psutil.net_connections()
    established_conxns = [cx for cx in conxns if cx[5] == 'ESTABLISHED']
    return established_conxns


def pid_to_command(pid):
    pass


def port_to_pid(port):
    pass


def main():
    pass


if __name__ == '__main__':
    main()

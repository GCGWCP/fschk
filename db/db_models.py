from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.ext.declarative import declared_attr


class File(object):
    __tablename__ = 'files'

    id = Column(Integer, primary_key=True)
    file_name = Column(String, nullable=True)
    full_path = Column(String, nullable=True)
    root_path = Column(String, nullable=True)
    size = Column(Integer, nullable=True)
    permissions = Column(Integer, nullable=True)
    created = Column(Float, nullable=True)
    last_modified = Column(Float, nullable=True)
    last_accessed = Column(Float, nullable=True)
    owner = Column(Integer, nullable=True)
    group = Column(Integer, nullable=True)
    inode = Column(Integer, nullable=True)
    file_type = Column(String, nullable=True)
    ext_attr = Column(String, nullable=True)
    sticky_bit = Column(Boolean, nullable=True)
    encoding = Column(String, nullable=True)
    sha256 = Column(String, nullable=True)
    sha512 = Column(String, nullable=True)

    # def __init__(self):
    #     self.id = ''
    #     self.file_name = ''
    #     self.root_path = ''
    #     self.size = ''
    #     self.permissions = ''
    #     self.created = ''
    #     self.last_modified = ''
    #     self.last_accessed = ''
    #     self.owner = ''
    #     self.group = ''
    #     self.inode = ''
    #     self.file_type = ''
    #     self.ext_attr = ''
    #     self.sticky_bit = ''
    #     self.encoding = ''
    #     self.sha256 = ''
    #     self.sha512 = ''

    #     return self

    def __repr__(self):
        return """<File (
file_name='%s',
full_path='%s',
root_path='%s',
size=%d,
permissions=%d,
created=%f,
last_modified=%f,
last_accessed=%f,
owner=%d,
group=%d,
inode=%d,
file_type=%d,
ext_attr='%s',
sticky_bit=%r,
encoding='%s',
sha256='%s',
sha512='%s')>""" % (
            self.file_name,
            self.full_path,
            self.root_path,
            self.size,
            self.permissions,
            self.created,
            self.last_modified,
            self.last_accessed,
            self.owner,
            self.group,
            self.inode,
            self.file_type,
            self.ext_attr,
            self.sticky_bit,
            self.encoding,
            self.sha256,
            self.sha512
        )


class FileSystem(object):
    __tablename__ = 'filesystem'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)

    def __repr__(self):
        return "<FileSystem (name='%s',)>" % (self.name)


class OS(object):
    __tablename__ = 'opsystems'

    id = Column(Integer, primary_key=True)
    uname = Column(String, nullable=True)
    apis = Column(JSON, nullable=True)

    def __repr__(self):
        return "<OS (uname='%s')>" % (self.uname)


class Process(object):
    __tablename__ = 'processes'

    id = Column(Integer, primary_key=True)
    user = Column(Integer, nullable=True)
    pid = Column(Integer, nullable=True)
    time_started = Column(DateTime, nullable=True)
    command = Column(String, nullable=True)

    def __repr__(self):
        return "<OS (pid='%s')>" % (self.pid)


class Kmod(object):
    __tablename__ = 'kernel_modules'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    version = Column(String, nullable=True)

    @declared_attr
    def file_location(cls):
        return(Column(Integer, ForeignKey(File.id)))

    # file_location = Column(Integer, ForeignKey(File.id), nullable=True)
    index = Column(Integer, nullable=True)
    references = Column(Integer, nullable=True)
    address = Column(String, nullable=True)
    uuid = Column(String, nullable=True)
    linked_against = Column(String, nullable=True)
    description = Column(String, nullable=True)

    def __repr__(self):
        return "<KernelModule (name='%s')>" % (self.name)


class Node(object):
    __tablename__ = 'node'

    id = Column(Integer, primary_key=True)
    # Link to Mongo Docs
    info = Column(String, nullable=True)

    def __repr__(self):
        return "<Info (name='%s')>" % (self.info)


class Device(object):
    __tablename__ = 'device'

    id = Column(Integer, primary_key=True)
    useragent = Column(String(254), nullable=True)
    language = Column(String(16), default='us_en')
    do_not_track = Column(Boolean, default=False)
    java_enabled = Column(Boolean, default=False)
    cookies_enabled = Column(Boolean, default=False)
    web_storage_enabled = Column(Boolean, default=False)
    request_headers = Column(String(), nullable=True)
    release_date = Column(DateTime, nullable=True)
    screen_width = Column(Integer, nullable=True)
    screen_height = Column(Integer, nullable=True)
    color_depth = Column(Integer, nullable=True)
    pixel_depth = Column(Integer, nullable=True)
    device_pixel_ratio = Column(Integer, nullable=True)
    timezone_offset = Column(Integer, nullable=True)
    plugins = Column(JSON, nullable=True)


    def __init__(self, useragent, language, do_not_track, java_enabled, cookies_enabled, web_storage_enabled, request_headers, release_date, screen_width, screen_height, specs):
        self.useragent = useragent
        self.language = language
        self.do_not_track = do_not_track
        self.java_enabled = java_enabled
        self.cookies_enabled = cookies_enabled
        self.web_storage_enabled = web_storage_enabled
        self.request_headers = request_headers
        self.release_date = release_date
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.specs = specs

    def __repr__(self):
        return "<Device (id='%d')>" % self.id


class TCPSYNPacketSignature(object):
    __tablename__ = 'tcp_syn_packet_sig'

    id = Column(Integer, primary_key=True)
    ip_ttl = Column(Integer, nullable=True)
    ip_tos = Column(Integer, nullable=True)
    ip_total_length = Column(Integer, nullable=True)
    ip_flags = Column(Integer, nullable=True)
    tcp_window_size = Column(Integer, nullable=True)
    # TODO: Determine whether to store individual options
    # or options segment of packet and parse elsewhere.
    tcp_options = Column(Integer, nullable=True)

    def __init__(self, ip_ttl, ip_tos, ip_total_length, ip_flags, tcp_window_size, tcp_options):
        self.ip_ttl = ip_ttl
        self.ip_tos = ip_tos
        self.ip_total_length = ip_total_length
        self.ip_flags = ip_flags
        self.tcp_window_size = tcp_window_size
        self.tcp_options = tcp_options

    def __repr__(self):
        return "<TCPSYNPacketSignature (id='%d')>" % self.id


class DNSFingerPrint(object):
    __tablename__ = 'dns_fingerprint'

    id = Column(Integer, primary_key=True)
    public_dns_ip = Column(Integer, nullable=True)
    public_dns_host = Column(String(128), nullable=True)
    ipv6_lookup = Column(Boolean, nullable=True)
    server_country = Column(Float, nullable=True)
    server_region = Column(Float, nullable=True)
    server_isp = Column(String(64), nullable=True)
    server_organization = Column(String(64), nullable=True)
    server_as_number = Column(String(64), nullable=True)
    server_domain = Column(String(64), nullable=True)
    provider = Column(String(64), nullable=True)

    def __init__(self, public_dns_ip, public_dns_host, ipv6_lookup, server_country, server_region, server_isp, server_organization, server_as_number, server_domain, provider):
        self.public_dns_ip = public_dns_ip
        self.public_dns_host = public_dns_host
        self.ipv6_lookup = ipv6_lookup
        self.server_country = server_country
        self.server_region = server_region
        self.server_isp = server_isp
        self.server_organization = server_organization
        self.server_as_number = server_as_number
        self.server_domain = server_domain
        self.provider = provider

    def __repr__(self):
        return "<DNSFingerPrint (id='%d')>" % self.id


class IPv4Address(object):
    __tablename__ = 'ipv4_addr'

    id = Column(Integer, primary_key=True)
    ipv4_addr_int = Column(Integer, nullable=True)

    def __init__(self, ipv4_addr):
        self.ipv4_addr = ipv4_addr

    def __repr__(self):
        return "<IPv4Address (id='%d')>" % self.id


# class Connection(object):
#     __tablename__ = 'connection'

#     @declared
#     id = Column(Integer, primary_key=True)
#     source = Column(ForeignKey(IPv4Address.id), nullable=True)
#     source_text = Column(String, nullable=True)
#     dest = Column(ForeignKey(IPv4Address.id), nullable=True)
#     dest_text = Column(String, nullable=True)

#     def __repr__(self):
#         return "<Connection (id='%d')>" % self.id


def main():
    pass


if __name__ == '__main__':
    main()

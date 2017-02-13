from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.dialects.postgresql import JSON


class File(object):
    __tablename__ = 'files'

    id = Column(Integer, primary_key=True)
    file_name = Column(String, nullable=True)
    root_path = Column(String, nullable=True)
    size = Column(Integer, nullable=True)
    permissions = Column(Integer, nullable=True)
    created = Column(DateTime, nullable=True)
    last_modified = Column(DateTime, nullable=True)
    last_accessed = Column(DateTime, nullable=True)
    owner = Column(Integer, nullable=True)
    group = Column(Integer, nullable=True)
    inode = Column(Integer, nullable=True)
    file_type = Column(String, nullable=True)
    ext_attr = Column(String, nullable=True)
    sticky_bit = Column(Integer, nullable=True)
    encoding = Column(String, nullable=True)
    sha256 = Column(String, nullable=True)
    sha512 = Column(String, nullable=True)

    def __repr__(self):
        return "<File (file_name='%s', root_path='%s', size='%d', permissions='%d', created='%s', last_modified='%s', last_accessed='%s', owner='%d', group='%d', inode='%d', file_type='%s', ext_attr='%s', sticky_bit='%s', encoding='%s', sha256='%s', sha512='%s')>" % (self.file_name, self.root_path, self.size, self.permissions, self.created, self.last_modified, self.owner, self.group, self.inode, self.created, self.last_modified, self.last_accessed, self.file_type, self.ext_attr, self.sticky_bit, self.encoding, self.sha256, self.sha512)


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

    def __repr__(self):
        return "<OS (uname='%s')>" % (self.uname)


class Process(object):
    __tablename__ = 'processes'

    id = Column(Integer, primary_key=True)
    pid = Column(Integer, nullable=True)

    def __repr__(self):
        return "<OS (pid='%s')>" % (self.pid)


class Kmod(object):
    __tablename__ = 'kernel_modules'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    file = Column(Integer, ForeignKey(File.id), nullable=True)

    def __repr__(self):
        return "<KernelModule (name='%s')>" % (self.name)


class Node(object):
    __tablename__ = 'node'

    id = Column(Integer, primary_key=True)
    # Link to Mongo Docs
    info = Column(String, nullable=True)

    def __repr__(self):
        return "<Info (name='%s')>" % (self.info)


class Device(Model):
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
        return '<id {}>'.format(self.id)


def main():
    pass


if __name__ == '__main__':
    main()

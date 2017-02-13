from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref


class File(Base):
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


def main():
    pass


if __name__ == '__main__':
    main()

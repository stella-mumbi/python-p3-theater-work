from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, create_engine, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

engine = create_engine('sqlite:///lib/theater.db', echo=True)


class Auditions(Base):
    __tablename__ = 'auditions'
    id = Column(Integer, primary_key=True)
    location = Column(String())
    phone = Column(Integer())
    hired = Column(Boolean())

    role_id = Column(Integer(), ForeignKey('roles.id'))
    role = relationship("Role", backref='auditions')

    def __rep__(self):
        return f"{self.id} - {self.location} - {self.phone} - {self.hired}"


class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    character_name = Column(String())

    audition = relationship("Auditions", backref='roles')

    def __rep__(self):
        return f"{self.id} - {self.character_name}"


Base.metadata.create_all(engine)
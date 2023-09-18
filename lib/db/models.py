from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)


class LicensePlate(Base):
    __tablename__ = 'license_plates'

    id = Column(Integer(), primary_key=True)
    plate_number = Column(String())
    owner_id = Column(Integer(), ForeignKey('owners.id'))
    make = Column(String())
    model_name = Column(String())
    model_year = Column(Integer())

    owners = relationship('Owner', backref=backref('owner_name'))


class Owner(Base):
    __tablename__ = 'owners'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    age = Column(Integer())
    address = Column(String())
    # vehicle_id = Column(Integer(), ForeignKey('license_plates.id'))
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
    model_id = Column(Integer(), ForeignKey('models.id'))

    def __repr__(self):
        return f'LicensePlate(id={self.id}, ' + \
            f'plate_number={self.plate_number}, ' + \
            f'owner_id={self.owner_id}, ' + \
            f'model_id={self.model_id})'

class Owner(Base):
    __tablename__ = 'owners'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    age = Column(Integer())
    address = Column(String())
    # vehicle_id = Column(Integer(), ForeignKey('license_plates.id'))
    
    license_plates = relationship('LicensePlate', backref=backref('owner'))

    def __repr__(self):
        return f'Owner(id={self.id}, ' + \
            f'name={self.name}, ' + \
            f'age={self.age}, ' + \
            f'address={self.address})'


class Make(Base):
    __tablename__ = 'makes'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    # vehicle_id = Column(Integer(), ForeignKey('license_plates.id'))
    
    models = relationship('Model', backref=backref('make'))

    def __repr__(self):
        return f'Make(id={self.id}, ' + \
            f'name={self.name}, '


class Model(Base):
    __tablename__ = 'models'

    id = Column(Integer(), primary_key=True)
    make_id = Column(Integer(), ForeignKey('makes.id'))
    name = Column(String())
    year = Column(Integer())
    
    license_plates = relationship('LicensePlate', backref=backref('model'))

    def __repr__(self):
        return f'Model(id={self.id}, ' + \
            f'make_id={self.make_id}, ' + \
            f'name={self.name}, ' + \
            f'year={self.year}, '
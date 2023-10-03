#!/usr/bin/env python3

from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import LicensePlate, Owner, Make, Model

if __name__ == '__main__':
    engine = create_engine('sqlite:///project_3.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(LicensePlate).delete()
    session.query(Owner).delete()
    session.query(Make).delete()
    session.query(Model).delete()

    fake = Faker()

    # makes = ['chevrolet', 'chrysler', 'dodge', 'ford', 'gmc', 'honda', 'hyundai', 'kia', 'maserati', 'nissan', 'toyota',]
    # should makes and models be combined? ex: ['nakamura si-7', 'watson r-turbo']
    # year ????

    makes = []
    makes_list = ['bennett', 'carson', 'hunter', 'krieger', 'nakamura', 'nmc', 'watson']
    for make_name in makes_list:
        make = Make(
            name=make_name
        )
        session.add(make)
        session.commit()
        makes.append(make)

    models = []
    models_list = ['cabrio', 'coupe', 'ev', 'fastback', 'hatch', 'minivan', 'pickup', 'sedan', 'sport', 'sport turbo', 'truck', "type 1", 'v6', 'v8', 'v10', 'v12', 'van']
    for model_name in models_list:
        model = Model(
            name=model_name,
            # make_id = Column(Integer(), ForeignKey('makes.id'))
            make_id=random.choice(makes).id,
            year=random.randint(1960, 2015)
        )

        session.add(model)
        session.commit()
        models.append(model)

    # reviews = []
    # for game in games:
    #     for i in range(random.randint(1,5)):
    #         review = Review(
    #             score=random.randint(0, 10),
    #             comment=fake.sentence(),
    #             game_id=game.id
    #         )

    #         reviews.append(review)

    owners = []
    for i in range(45):
        owner = Owner(
            name=fake.unique.name(),
            age=random.randint(16, 80),
            address=fake.address()
        )
    
    license_plates = []
    for i in range(50):
        license_plate = LicensePlate(
            owner=fake.unique.name(),
            make=random.choice(makes),
            model=random.choice(models),
            year=random.randint(1990, 2023)
        )

        session.add(license_plate)
        session.commit()

        license_plates.append(license_plate)
    
    session.bulk_save_objects(makes)
    session.bulk_save_objects(models)
    session.bulk_save_objects(owners)
    session.bulk_save_objects(license_plates)
    session.commit()
    session.close()
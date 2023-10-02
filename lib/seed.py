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

    makes = ['bennett', 'carson', 'hunter', 'krieger', 'nakamura', 'nmc', 'watson']
    models = ['annihilator', 'si-7', 'r-turbo']

    reviews = []
    for game in games:
        for i in range(random.randint(1,5)):
            review = Review(
                score=random.randint(0, 10),
                comment=fake.sentence(),
                game_id=game.id
            )

            reviews.append(review)

    
    license_plates = []
    for i in range(50):
        license_plate = LicensePlate(
            owner=fake.unique.name(),
            make=random.choice(makes),
            model=random.choice(models),
            year=random.randint(1990, 2023)
        )

        # add and commit individually to get IDs back
        session.add(license_plate)
        session.commit()

        license_plates.append(license_plate)
    
    session.bulk_save_objects(reviews)
    session.commit()
    session.close()

    
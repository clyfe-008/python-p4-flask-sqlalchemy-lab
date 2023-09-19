#!/usr/bin/env python3

from random import choice as rc
from faker import Faker
from app import app, db
from models import Zookeeper, Animal, Enclosure

fake = Faker()


with app.app_context():

    # Create the tables
    db.create_all()

    zookeepers = []
    for n in range(25):
        zk = Zookeeper(
            name=fake.first_name(),
            birthday=fake.date_of_birth(minimum_age=18, maximum_age=70)
        )
        zookeepers.append(zk)

    db.session.add_all(zookeepers)

    enclosures = []
    environments = ['Grass', 'Sand', 'Water']

    for n in range(25):
        e = Enclosure(
            environment=rc(environments),
            open_to_visitors=rc([True, False])
        )
        enclosures.append(e)

    db.session.add_all(enclosures)

    animals = []
    species = ['Lion', 'Tiger', 'Bear', 'Hippo', 'Rhino', 'Elephant', 'Ostrich', 'Snake', 'Monkey']

    for n in range(200):
        name = fake.first_name()
        while name in [a.name for a in animals]:
            name = fake.first_name()
        a = Animal(
            name=name,  
            species=rc(species),  
            zookeeper=rc(zookeepers),
            enclosure=rc(enclosures)  )
        animals.append(a)

    db.session.add_all(animals)
    db.session.commit()

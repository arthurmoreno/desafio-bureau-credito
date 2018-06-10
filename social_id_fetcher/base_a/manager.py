import random

from sqlalchemy.orm import sessionmaker
from  sqlalchemy.sql.expression import func, select
from pycpfcnpj.gen import cpf as cpf_generator

from base_a.connection import get_engine
from base_a.models import People
from base_a.utils import name_generator, address_generator


PEOPLE_COUNT = 1000


class Manager(object):
    def __init__(self, *args, **kwargs):
        self.engine = get_engine()

    def drop_models_tables(self):
        People.__table__.drop(bind=get_engine(), checkfirst=True)

    def create_models_tables(self):
        People.__table__.create(bind=get_engine(), checkfirst=True)
    
    def restart_models_tables(self):
        self.drop_models_tables()
        self.create_models_tables()
    
    def get_people(self, cpf):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session.query(People).filter_by(cpf=cpf).first()
    
    def get_random_people(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session.query(People).offset(
            int(PEOPLE_COUNT*random.random())).first()
    
    def generate_people(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()

        peoples = []
        for _ in range(PEOPLE_COUNT):
            peoples.append(People(
                cpf=cpf_generator(),
                name=name_generator(),
                address=address_generator()
            ))
        session.add_all(peoples)
        session.commit()

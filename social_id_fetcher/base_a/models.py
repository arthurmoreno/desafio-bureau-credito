from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()

class People(Base):
    __tablename__ = 'people'

    cpf = Column(String, primary_key=True)
    name = Column(String)
    address = Column(String)
    # lista de dividas -- todo -- = Column(String)

    def __repr__(self):
        return f'<Person(cpf={self.cpf}, name={self.name})>'

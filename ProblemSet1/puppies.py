from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()

class Shelter(Base):
    __tablename__ = 'shelter'
    id = Column(Integer, primary_key = True)
    name =Column(String(80), nullable = False)
    address = Column(String(250))
    city = Column(String(80))
    state = Column(String(30))
    zipCode = Column(String(10))
    website = Column(String)
    
class Puppy(Base):
    __tablename__ = 'puppy'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(6), nullable = False)
    dateOfBirth = Column(Date)
    picture = Column(String)
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship(Shelter)
    weight = Column(Numeric(10))

    def __repr__(self):
        return '{}:{} {} {} {} {}'.format(self.__class__.__name__,
                                self.name,
                                self.id,
                                self.gender,
                                self.dateOfBirth,
                                self.weight)

    def __cmp__(self, other):
        if hasattr(other, 'name'):
            return self.name.__cmp__(other.name)

    def getKey(self):
        return self.name


engine = create_engine('sqlite:///puppyshelter.db')
 

Base.metadata.create_all(engine)
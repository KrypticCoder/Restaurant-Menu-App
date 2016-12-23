import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship   # Needed to create foreign key relationship

from sqlalchemy import create_engine

# Lets sqlalchemy know our classes correspond to tables in db
Base = declarative_base()   

class Restaurant(Base):
    __tablename__ = 'restaurant'
    name = Column(String(250), nullable=False)
    id = Column(Integer, primary_key=True)

class MenuItem(Base):
    __tablename__ = 'menu_item'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

    @property 
    def serialize(self):
        # Returns object data in easily serializable format
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course
        }
        



# Engine points to database we will use
engine = create_engine('sqlite:///restaurantmenu.db')   

# Adds classes as tables in our db
Base.metadata.create_all(engine) 


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem  # Existing database
engine = create_engine('sqlite:///restaurantmenu.db')  # Lets program know which database 
                                                    # engine we want to communicate with

Base.metadata.bind = engine # Connects class connections to tables in db

DBSession = sessionmaker(bind = engine)     # Establishes link of communication 
                                            # b/w code executions and engine

'''
In order to perform CRUD on our db, SQLAlchemy executes operations via 
interface called session. Session allows us to write down all commands 
we want to execute but not send them to database until we call session.commit
'''

session = DBSession() # Staging area for all objects loaded into database session object 

mcdonalds = session.query(Restaurant).filter_by(name = 'McDonalds').all()
for mac in mcdonalds:
    session.delete(mac)
session.commit()

##### INSERTING #####
print("Inserting values into db...")

# Perform insert on Restaurant table
myFirstRestaurant = Restaurant(name = "Pizza Palace")
session.add(myFirstRestaurant) 
session.commit() 

mySecondRestaurant = Restaurant(name = "McDonalds")
session.add(mySecondRestaurant)
session.commit

# Perform insert on MenuItem table
cheesepizza = MenuItem(name = "Cheese Pizza", description = "Made with all natural ingredients and fresh mozzarella", course = "Entree", price = "$8.99", restaurant = myFirstRestaurant)
session.add(cheesepizza)
session.commit()
print('Items inserted')
print('\n')

##### QUERYING ##### 
print('Querying db...')
# list of all objects in Restaurants and MenuItem tables
all_restaurants = session.query(Restaurant).all()  
all_items = session.query(MenuItem).all()

# Extract first object from query
firstRestaruant = session.query(Restaurant).first()
firstRestaruant.name
firstItem = session.query(MenuItem).first()
firstItem.name

print('first and only restaurant: ' + firstRestaruant.name)
print('first and only item: ' + firstItem.name)
print('\n')


##### UPDATING #####
print('Updating values in db...')
secondRestaurant = session.query(Restaurant).filter_by(name = 'McDonalds').one()
print(secondRestaurant.name)
secondRestaurant.name = 'Panera Bread' 
print('Restaurant name changed to ' + secondRestaurant.name)
session.add(secondRestaurant)
session.commit()
print('\n')


##### DELETING #####
print('Deleting values from db... ')

##### Delete items from db #####
for restaurant in all_restaurants:
    session.delete(restaurant)
for item in all_items:
    session.delete(item)
session.commit()

# Database should be empty now
all_restaurants = session.query(Restaurant).all()
all_items = session.query(MenuItem).all()
if len(all_restaurants) == 0:
    print("Restaurant table is empty")
else:
    print("Restaurant table still holds tuples")
    for rest in all_restaurants:
        print(rest.name)

if len(all_items) == 0:
    print("MenuItem table is empty")
else:
    print("MenuItem table still holds tuples")
    for item in all_items:
        print(item.name)









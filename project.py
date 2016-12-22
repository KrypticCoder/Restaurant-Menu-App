from flask import Flask
# Create instance of this class with name of running app
app = Flask(__name__)

# Import the database we created in first lesson
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create session and connect to DB ##
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).first()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    output = ''
    for i in items:
        output += i.name
        output += '</br>'
        output += i.price
        output += '</br>'
        output += i.description
        output += '</br>'
        output += '</br>'


    return output




# Server only runs if script is executed directly from Python interpreter 
# and not used as imported module 
if __name__ == '__main__':
    # User of app can execute arbitrary python code on your computer
    app.debug = True

    # Server only accessible from host machine 
    # Using a vagrant env, so we must make our server publicly available
    app.run(host = '0.0.0.0', port=5000) # Listen on all public IP addresses


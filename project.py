# Message flashing is a feature that will prompt a message to the user 
# immediately after certain action has taken place then
from flask import Flask, render_template, request, redirect, url_for, flash
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
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    return render_template('menu.html',restaurant=restaurant,items=items)


@app.route('/restaurants/<int:restaurant_id>/new/', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        newItem = MenuItem(name=request.form['name'], description=request.form['description'], 
                            price=request.form['price'], course=request.form['course'], 
                            restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        flash("Menu item \'%s\' created" % newItem.name)
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('newmenuitem.html', restaurant_id=restaurant_id)

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    editItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        if request.form['name']:
            flash("Menu item \'%s\' has been changed to \'%s\'" % (editItem.name, request.form['name']))
        else:
            flash("Menu item \'%s\' has been changed" % editItem.name)
        editItem.name = request.form['name'] if request.form['name'] else editItem.name
        editItem.description = request.form['description'] if request.form['description'] else editItem.description
        editItem.price = request.form['price'] if request.form['price'] else editItem.price
        editItem.course = request.form['course'] if request.form['course'] else editItem.course
        session.add(editItem)
        session.commit()
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('editmenuitem.html', item=editItem)

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    deleteItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        session.delete(deleteItem)
        session.commit()
        flash("Menu item \'%s\' deleted" % deleteItem.name)
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('deletemenuitem.html', item=deleteItem)


# Server only runs if script is executed directly from Python interpreter 
# and not used as imported module 
if __name__ == '__main__':
    # User of app can execute arbitrary python code on your computer
    app.debug = True

    # Flask uses a secret_key to create sessions for our user
    # Should be kept in separate file normally
    app.secret_key = 'super_secret_key'

    # Server only accessible from host machine 
    # Using a vagrant env, so we must make our server publicly available
    app.run(host = '0.0.0.0', port=5000) # Listen on all public IP addresses


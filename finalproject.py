from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
# Create instance of this class with name of running app
app = Flask(__name__)

@app.route('/')
@app.route('/restaurants/')
def showRestaurants():
    return ("This page will show all my restaurants")

@app.route('/restaurant/new/')
def newRestaurant():
    return ("This page is for making a new restaurant")

@app.route('/restaurant/<int:restaurant_id>/edit/')
def editRestaurant(restaurant_id):
    return ("This page will be for editing restaurant %s" % restaurant_id)


@app.route('/restaurant/<int:restaurant_id>/delete/')
def deleteRestaurant(restaurant_id):
    return ("This page will be for deleting restaurant %s" % restaurant_id)


@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu')
def showMenu(restaurant_id):
    return ("This page is the menu for restaurant %s" % restaurant_id)


@app.route('/restaurant/<int:restaurant_id>/menu/new/')
def newMenuItem(restaurant_id):
    return ("This page is for making a new menu item for restaurant %s" % restaurant_id)

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit')
def newMenuItem(restaurant_id, menu_id):
    return ("This page is for editing menu item %s" % menu_id)

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete')
def newMenuItem(restaurant_id, menu_id):
    return ("This page is for deleting menu item %s" % menu_id)


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

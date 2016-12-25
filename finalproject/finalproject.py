from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
# Create instance of this class with name of running app
app = Flask(__name__)

#Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}
restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]

#Fake Menu Items
items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}

# Show all restaurants 
@app.route('/')
@app.route('/restaurants/')
def showRestaurants():
    return render_template('restaurants.html', restaurants=restaurants)

# Create a new restaurant
@app.route('/restaurant/new/', methods=['GET', 'POST'])
def newRestaurant():
    return render_template('newrestaurant.html')

# Edit a restaurant
@app.route('/restaurant/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    return render_template('editrestaurant.html', restaurant=restaurant)

# Delete a restaurant
@app.route('/restaurant/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    return render_template('deleterestaurant.html', restaurant=restaurant)

# Show a restaurant's menu
@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu')
def showMenu(restaurant_id):
    return render_template('menu.html', restaurant=restaurant, items=items)

# Create a new menu item for a restaurant
@app.route('/restaurant/<int:restaurant_id>/menu/new/', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    return render_template('newmenuitem.html')

# Edit a menu item for a restaurant
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    return render_template('editmenuitem.html', restaurant=restaurant, item=item)

# Delete a menu item for a restaurant
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    return render_template('deletemenuitem.html', restaurant=restaurant, item=item)


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

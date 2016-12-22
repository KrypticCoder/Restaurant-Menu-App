# HTTPServer stores server address as instance variables named server_name and server_port
# BaseHTTPRequestHandler used to handle requests that arrive at server
#     Must be subclassed to handle each request method
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

# A CGI (Common Gateway Interface) script is invoked by HTTP server to process user input 
# submited through HTML <FORM> or <ISINDEX> element. A cgi provides an easier way to handle data 
# from server to client rather than the 'query string' that is part of the URL
import cgi

# import the database we created in first lesson
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create session and connect to DB ##
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            #########################################
            # List all of the restaurants in the db #
            #########################################
            if self.path.endswith("/restaurants"):
                
                # Successful GET request
                self.send_response(200)
                # Inform client we are replying with text in the form of html
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                # Get all restaurants stored in db
                restaurants = session.query(Restaurant).all()
                
                output = ""
                # Provide link to create a new restaurant
                output += "<a href = '/restaurants/new' > Make a New Restaurant Here </a></br></br>"
               
                for restaurant in restaurants:
                    output += restaurant.name
                    output += "</br>"

                    # Provide link to edit each restaurant listed
                    output += "<a href ='/restaurants/%s/edit' >Edit </a> " % restaurant.id
                    output += "</br>"

                    # Provide link to delete each restaurant listed
                    output += "<a href ='/restaurants/%s/delete'> Delete </a>" % restaurant.id
                    output += "</br></br></br>"

                output += "</body></html>"
                self.wfile.write(output)
                return

            ###########################
            # Create a new restaurant #
            ###########################
            if self.path.endswith("/restaurants/new"):

                # Successful GET request
                self.send_response(200)
                # Inform client we are replying with text in the form of html
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "<h1>Make a New Restaurant</h1>"
                output += "<form method='POST' enctype='multipart/form-data' action ='/restaurants/new' >"
                output += "<input name='newRestaurantName' type='text' placeholder='New Restaurant Name' > "
                output += "<input type='submit' value='Create'>"
                output += "</form></html></body>"
                self.wfile.write(output)
                return

            ###############################
            # Edit an existing restaurant #
            ###############################
            if self.path.endswith("/edit"):

                # Get the restaurant id from the URL: localhost:8080/restaurant/id/edit
                editRestaurantID = self.path.split("/")[2]
                print('edit restaurant id ' + str(editRestaurantID))

                # Find the restaurant we want to edit
                editRestaurant = session.query(Restaurant).filter_by(id=editRestaurantID).one()

                print('edit restaurant ' + str(editRestaurant.name))
                
                # if restaurant exists
                if editRestaurant:
                    print('found restaurant')
                    # Successful GET request
                    self.send_response(200)
                    # Inform client we are replying with text in the form of html
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    print('render html')
                    output = "<html><body>"
                    output += "<h1>"
                    output += editRestaurant.name
                    output += "</h1>"
                    output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/edit' >" % editRestaurantID
                    output += "<input name='newRestaurantName' type='text' placeholder='%s' >" % editRestaurant.name
                    output += "<input type='submit' value='Rename'>"
                    output += "</form>"
                    output += "</body></html>"
                    self.wfile.write(output)

            #################################                             
            # Delete an existing restaurant # 
            #################################
            if self.path.endswith("/delete"):

                # Get the restaurant id from the URL: localhost:8080/restaurant/id/delete
                deleteRestaurantID = self.path.split("/")[2]

                # Find the restaurant we want to delete
                deleteRestaurant = session.query(Restaurant).filter_by(id=deleteRestaurantID).one()
                
                # If restaurant exists
                if deleteRestaurant:

                    # Successful GET request
                    self.send_response(200)
                    # Inform client we are replying with text in the form of html
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()

                    output = ""
                    output += "<html><body>"
                    output += "<h1>Are you sure you want to delete %s?" % deleteRestaurant.name
                    output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/delete'>" % deleteRestaurantID
                    output += "<input type='submit' value='Delete'>"
                    output += "</form>"
                    output += "</body></html>"
                    self.wfile.write(output)

        except IOError:
            self.send_error(404, "File Not Found %s" % self.path) # GET request results in error


    def do_POST(self):
        try:
            ###################################
            # POST request for new restaurant #
            ###################################
            if self.path.endswith("/restaurants/new"):

                # HTML form header, content-type, is parsed into main value & dictionary of parameters
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))

                # Check to see if main value is form data being received
                if ctype == 'multipart/form-data':

                    # Collect all of the fields in a form
                    fields = cgi.parse_multipart(self.rfile, pdict)

                    # Take the value of a specific field(s) and store it in an array
                    messagecontent = fields.get('newRestaurantName')

                    # Create new Restaurant object
                    newRestaurant = Restaurant(name=messagecontent[0])
                    session.add(newRestaurant)
                    session.commit()

                    # Successful POST request
                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')

                    # redirect back to homepage
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

            #########################################
            # POST request for editing a restaurant #
            #########################################
            if self.path.endswith("/edit"):

                # form header split into main value & dictionary of parameters
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))

                # Verify we are receiving form data
                if ctype == 'multipart/form-data':

                    # Collect all fields in form
                    fields = cgi.parse_multipart(self.rfile, pdict)

                    # Store value of field in array
                    messagecontent = fields.get('newRestaurantName')

                    # Find the ID of the restaurant we chose to edit
                    editRestaurantID = self.path.split("/")[2]

                    # Use that ID to find the restaurant
                    editRestaurant = session.query(Restaurant).filter_by(id=editRestaurantID).one()
                    
                    # if restaurant exists
                    if editRestaurant:
                        editRestaurant.name = messagecontent[0]
                        session.add(editRestaurant)
                        session.commit()

                        # Successful POST request
                        self.send_response(301)
                        self.send_header('Content-type', 'text/html')

                        # Redirect back to home page
                        self.send_header('Location', '/restaurants')
                        self.end_headers()

            ##########################################
            # POST request for deleting a restaurant #
            ##########################################
            if self.path.endswith("/delete"):

                # Find the id of the restaurant we chose to delete
                deleteRestaurantID = self.path.split("/")[2]

                # Use that id to find the restaurant
                deleteRestaurant = session.query(Restaurant).filter_by(id=deleteRestaurantID).one()
                
                # if restaurant exists
                if deleteRestaurant:
                    session.delete(deleteRestaurant)
                    session.commit()

                    # Successful POST request
                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')

                    # Redirect back to home page
                    self.send_header('Location', '/restaurants')
                    self.end_headers()
        except:
            pass

def main():
    try:
        port = 8080

        # HTTPServer(server_address, RequestHandlerClass)
        # server_address contains host (empty string), and port number (8080)
        server = HTTPServer(('', port), webserverHandler)
        print "Web server running ... open localhost:%s/restaurants in your browser" % str(port)
        server.serve_forever()

    except KeyboardInterrupt:
        print "^C entered, stopping web server..."
        server.socket.close()


if __name__ == '__main__':
    main()


# HTTPServer stores server address as instance variables named server_name and server_port
# BaseHTTPRequestHandler used to handle requests that arrive at server
#     Must be subclassed to handle each request method
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

# A CGI (Common Gateway Interface) script is invoked by HTTP server to process user input 
# submited through HTML <FORM> or <ISINDEX> element. A cgi provides an easier way to handle data 
# from server to client rather than the 'query string' that is part of the URL
import cgi 

class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith('/hello'):
                self.send_response(200)     # Successful GET request

                # Inform client we are replying with text in the form of html
                self.send_header('Content-type', 'text/html')  
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "Hello!"

                # Refer to ***
                output += "<form method='POST' enctype='multipart/form-data' action='/hello'> \
                            <h2>What would you like me to say?</h2><input name='message' type='text'> \
                            <input type='submit' value='Submit'> </form>"
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return

            if self.path.endswith('/hola'):
                self.send_response(200)     

                self.send_header('Content-type', 'text/html')  
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "&#161Hola! <a href = '/hello'>Back to Hello</a>"
                # Refer to ***
                output += "<form method='POST' enctype='multipart/form-data' action='/hello'> \
                            <h2>What would you like me to say?</h2><input name='message' type='text'> \
                            <input type='submit' value='Submit'> </form>"
                output += "</body></html>"
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return

        except IOError:
            self.send_error(404, "File Not Found %s" % self.path) # GET request results in error


    def do_POST(self):
        try:
            self.send_response(301)  # Used for permanent redirection
            self.end_headers()

            # parse_header() parses HTML form header, such as content-type into main value and dictionary of parameters
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))

            # Check to see if this is form data being received 
            if ctype == 'multipart/form-data':

                # Collect all of the fields in a form
                fields = cgi.parse_multipart(self.rfile, pdict)

                # Get out the value of a specific field(s) and store it/them in an array
                messagecontent = fields.get('message')

                output = ""
                output += "<html><body>"
                output += "<h2> Okay, how about this: </h2>"
                output += "<h1> %s </h1>" % messagecontent[0]

                #######  ***  #######
                # Add post request along with header tag to prompt user to input data 
                # Note: input field coincides with the message field we are extracting data from in the POST request
                output += "<form method='POST' enctype='multipart/form-data' action='/hello'> \
                            <h2>What would you like me to say?</h2><input name='message' type='text'> \
                            <input type='submit' value='Submit'> </form>"
                output += "</body><html>"
                self.wfile.write(output)
                print output

        except:
            pass

def main():
    try:
        port = 8080

        # HTTPServer(server_address, RequestHandlerClass)
        # server_address contains host (empty string), and port number (8080)
        server = HTTPServer(('', port), webserverHandler)
        print "Web server running on port %s" % port
        server.serve_forever()

    except KeyboardInterrupt:
        print "^C entered, stopping web server..."
        server.socket.close()


if __name__ == '__main__':
    main()


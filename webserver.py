# HTTPServer stores server address as instance variables named server_name and server_port
# BaseHTTPRequestHandler used to handle requests that arrive at server
#     Must be subclassed to handle each request method
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith('/hello'):
                self.send_response(200)     # Successful GET request
                self.send_header('Content-type', 'text/html')  # Inform client we are replying with text in the form of html
                self.end_headers()

                output = ""
                output += "<html><body>Hello!</body></html>"
                self.wfile.write(output)
                print output
                return
        except IOError:
            self.send_error(404, "File Not Found %s" % self.path) # GET request results in error


def main():
    try:
        port = 8080

        # HTTPServer(server_address, RequestHandlerClass)
        # server_address contains host (empty string) and port number (8080)
        server = HTTPServer(('', port), webserverHandler)
        print "Web server running on port %s" % port
        server.serve_forever()

    except KeyboardInterrupt:
        print "^C entered, stopping web server..."
        server.socket.close()


if __name__ == '__main__':
    main()


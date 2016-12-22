# Need to append the subdirectory to our current path in order to access our previous db files
# Python only checks up a directory tree, not down 
import sys
sys.path.append("./IntroToSQLAlchemy/")


from flask import Flask
# Create instance of this class with name of running app
app = Flask(__name__)


@app.route('/')
@app.route('/hello')
def HelloWorld():
    return "Hello World"


# Server only runs if script is executed directly from Python interpreter 
# and not used as imported module 
if __name__ == '__main__':
    # User of app can execute arbitrary python code on your computer
    app.debug = True

    # Server only accessible from host machine 
    # Using a vagrant env, so we must make our server publicly available
    app.run(host = '0.0.0.0', port=5000) # Listen on all public IP addresses


# import the Flask class from the flask package
from flask import Flask

# create the application object
app = Flask(__name__)

# error handling
app.config["DEBUG"] = True

# use the decorator pattern to linke the view function to a url
@app.route('/')
@app.route("/hello")

# define the view using a function, which returns a string
def hello_world():
    return 'Hello Orville!'

@app.route("/test/<search_query>")
def search(search_query):
    return search_query



@app.route("/name/<name>")
def index(name):
    if name.lower() == "michael" :
        return "Hello, {}".format(name), 200
    else :
        return "Not Found", 404

if __name__ == '__main__':
    app.run()

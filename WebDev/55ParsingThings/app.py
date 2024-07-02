from flask import Flask

app = Flask(__name__)

# Making decorator functions for bold
def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"

    return wrapper_function

def make_heading(function):
    def wrapper():
        return f"<h1>{function()}</h1>"

    return wrapper

@app.route("/")
@make_bold
@make_heading
def hello_world():
    return "Hello World"

# This below is the way to use and pass variables 
@app.route("/<name>")
def greet_person(name):
    return f"Hello {name}"

if __name__ == "__main__":
    # This debugger is set to true so that whenever we make changes 
    # the server is reloaded on it's own
    app.run(debug=True)
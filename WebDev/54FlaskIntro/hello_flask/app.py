from flask import Flask

app = Flask(__name__)
# This __name__ is basically "__main__"
# __main__ basically provides an entry point to your code just like main() in other langs

# __main__
# In Python,
# __main__ is a variable that can hold different values depending on how the script is executed. 
# It's set to '__main__' when the script is run directly, but a different value (usually the script's module name) when it's imported as a module.

# This is a decorator function which only executes the below function when '/' is accessed
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Creating another decorator
@app.route("/bye")
def bye_bye():
    return "<p>Bye Bye!!</p>"

# To Run our app directly we can do this
if __name__ == "__main__":
    app.run()
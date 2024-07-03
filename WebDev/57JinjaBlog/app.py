from flask import Flask, render_template
from datetime import date

# Getting current year
current_year = date.today().year

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html", curr_year=current_year)

if __name__ == "__main__":
    app.run(debug=True)
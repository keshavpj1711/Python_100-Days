from os import name
from flask import Flask, render_template
from datetime import date
import requests
from requests.models import requote_uri

# Getting current year
current_year = date.today().year

# Predicting age and gender using apis
def predict_age_gender(name):
    genderize_endpoint = f"https://api.genderize.io?name={name}"
    agify_endpoint = f"https://api.agify.io?name={name}"
    
    gender_response = requests.get(url=genderize_endpoint)
    gender_response.raise_for_status()
    
    age_response = requests.get(url=agify_endpoint)
    age_response.raise_for_status()
    
    gender = gender_response.json()["gender"]
    age = age_response.json()["age"]
    
    info = {
        "name":name,
        "age":age,
        "gender":gender,
    }
    
    return info

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html", curr_year=current_year)

# To get our guess gender and age functionality
@app.route("/guess/<name>")
def guess_age_gender(name):
    return render_template("guess.html", guess_info=predict_age_gender(name))

if __name__ == "__main__":
    app.run(debug=True)
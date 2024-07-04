from flask import Flask, render_template
import requests

app = Flask(__name__)

# Getting blogs from ou api 
def get_blogs():
    api_endpoint = "https://api.npoint.io/c790b4d5cab58020d391"

    response = requests.get(url=api_endpoint)
    response.raise_for_status()

    blog_data = response.json()

    return blog_data

@app.route("/")
def home_page():
    return render_template("index.html", blogs=get_blogs())

if __name__ == "__main__":
    app.run(debug=True)
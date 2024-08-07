from flask import Flask, render_template
import requests

# Getting blog post data
api_endpoint = "https://api.npoint.io/c790b4d5cab58020d391"
blogs_data = requests.get(url=api_endpoint).json()

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html", blogs=blogs_data)


@app.route("/blog/<int:blog_id>")
def show_blog(blog_id):
    clicked_post = None
    for posts in blogs_data:
        if posts["id"] == blog_id:
            clicked_post = posts

    return render_template("post.html", post=clicked_post)

if __name__ == "__main__":
    app.run(debug=True)
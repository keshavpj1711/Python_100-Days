from flask import Flask, render_template
# Calling class
from post import Post

# Creating instance of that class
posts = Post()

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html", blogs=posts.get_blogs())

@app.route("/post/blog/<blog_id>")
def blogs(blog_id):
    return render_template("post.html")

if __name__ == "__main__":
    app.run(debug=True)
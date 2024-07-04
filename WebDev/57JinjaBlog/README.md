# How to use Python Code in html file?

Let say we are rendering `index.html` in our flask app.
Then we can pass any number of arguements in the `index.html` which can be used in it, this is done as shown below.

For example: 

```python
render_template("index.html", num=var_to_be_passed)
# This num keyword can be accesed in index.html 
```

### How can we actually use this in `index.html` but?

```html
<h1>This is the value of num = {{num}}</h1>
```

These `{{}}` can basically render the python code which is put inside them. so not only this we can put actually python code here.


# How to use multiline statements in jinja?

A basic stuff to remember here is that:

- `{% ... %}` for Statements
- `{{ ... }}` for Expressions to print to the template output
- `{# ... #}` for Comments not included in the template output

Example: Using **for loop** and **if** statement in jinja:

```jinja
{% for post in blogs: %}
{% if post["id"] == 2: %}
<h1>{{post["title"]}}</h1>
<h2>{{post["subtitle"]}}</h2>
{% endif %}
{% endfor %}
```

# URL Building with Flask

This basically helps to move to a required url where we want to go.
To build a URL to a specific function, use the `url_for()`.

Here's an example to know everything:

```python
from flask import url_for

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/')) # This basically redirects to /login?next=/
    print(url_for('profile', username='John Doe')) # This redirects to /user/John%Doe
```

>Learnt a lot with the last example where we have to create that blog thing and render same post.html but with different logic for different blogs
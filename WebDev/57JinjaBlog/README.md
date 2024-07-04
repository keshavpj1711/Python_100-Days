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
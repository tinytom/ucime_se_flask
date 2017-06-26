import os

# We are importing 'Flask' to create an application,
# 'render_template' to render the given template as the response

from flask import Flask, render_template


# Create a flask app and set a random secret key
app = Flask(__name__)
app.secret_key = os.urandom(24)

# / route and its view. This renders the index.html template


@app.route('/')
def index():
    return render_template('index.html')

# Illustration of a single view handling multiple routes


@app.route('/route1/')
@app.route('/route2/')
@app.route('/lengthy/route3/')
def multiple_routes():
    message = "A single view can handle multiple routes"
    return render_template('page.html', message=message)

# Illustration of the difference between route with and without a trailing
# slash


@app.route('/no-slash')
@app.route('/slash/')
def trailing_slash():
    message = "If the route URL has a trailing slash, there will be a redirect from the same URL without / to the one with /. If there is no trailing slash, this view will not handle the URL with trailing /."
    return render_template('page.html', message=message)

# Illustration of capturing variable data from the URL


@app.route('/message/<msg>/')
def capture_value(msg):
    message = "Variable parts in the route can be specified with angular brackets and a variable name. They will be captured using the specified name. "
    message += "Value captured in this view is the message - %s" % (msg)
    return render_template('page.html', message=message)

# Illustration of capturing variable data from the URL and converting it
# to a type


@app.route('/users/<int:userid>/')
def capture_value_int(userid):
    message = "It is possible to capture variable parts and convert to various type. Here we are using int. Others are string (default), path, float"
    return render_template('page.html', message=message)

# Illustration of specifying which HTTP methods a view handles for a route


@app.route('/method/get/', methods=['GET'])
def handle_get_only():
    message = "It is possible to specify the methods a view will handle. This view handles only GET. Defaults are GET, HEAD and OPTIONS"
    return render_template('page.html', message=message)


# Illustration of default values for the value captured from the URL
@app.route('/page/', defaults={'page': 1})
@app.route('/page/<int:page>/')
def show_page(page):
    message = "This is page number %d. If no page number is specified, the view defaults to page 1" % page
    return render_template('page.html', message=message)


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("80")
    )

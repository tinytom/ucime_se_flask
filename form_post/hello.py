from flask import Flask, make_response, request, render_template

app = Flask(__name__)
"""
docs
http://code.runnable.com/UhLMQLffO1YSAADK/handle-a-post-request-in-flask-for-python
http://flask.pocoo.org/docs/0.12/quickstart/#rendering-templates
"""
#handluj 404, posila zpet string "404", da se pouzit pro custom 404 stranku
@app.errorhandler(404)
def not_found(error):
    return make_response('404')

#loadni externi template (html), ocekava tyto stranky ve slozce 'templates'
@app.route('/')
def form():
    return render_template('form_submit.html')

#endpoint pro informace z formulare
@app.route('/hello/', methods=['POST'])
def hello():
    name = request.form['yourname']
    email = request.form['youremail']
    return render_template('form_action.html', name=name, email=email)


if __name__ == '__main__':
    app.run(debug=True)

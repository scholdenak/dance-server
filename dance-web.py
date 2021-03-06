from flask import Flask, redirect, request, render_template, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined

app = Flask(__name__)

# will cause jinja to throw errors like python
app.jinja_env.undefined = StrictUndefined

# causes jinja to auto reload when they have been changed. really intensive only use while debugging
app.jinja_env.auto_reload = True

# required to use flask sessions and debug toolbar
app.secret_key = "liurehtg36$;oaeurhnft;o5^a8s&(ei'fpq3wowrjfnghy"

FEEL_GOODS = {
    'motivate1' : {
        'quote' : 'Think Bigger',
        'author' : 'Robert Holden',
    },
    'motivate2' : {
        'quote' : 'Your limitation - It\'s only your imagination',
        'author' : 'unknown',
    },
    'motivate3' : {
        'quote' : "It's ok to be a glowstick: Sometimes we have to break before we shine",
        'name' : 'Jadah Sellner'
    },
}

@app.route('/')
def go_to_homepage():
    """directs to homepage"""

    return render_template('homepage.html')

@app.route('/get-name')
def session_get_name():

    name = request.args.get('name')
    session['name'] = name
    return redirect('/step-two')

@app.route('/step-two')
def pull_up_page_two():

    return render_template('base-temp.html',
                            name=session['name'])



if __name__ == '__main__':
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    DebugToolbarExtension(app)

    app.run(host='0.0.0.0')

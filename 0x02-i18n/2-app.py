#!/usr/bin/env python3
"""instantiate the Babel object in your app"""
from flask import Flask, render_template, request
from flask_babel import Babel

class Config(object):
    DEBUG = True
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@app.route('/')
def index():
    """index"""
    return render_template('1-index.html')

@babel.localeselector
def get_locale():
    """Use request.accept_languages to determine
    the best match with our supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

if __name__ == "__main__":
    """ Main Function """
    app.run()
#!/usr/bin/env python3
"""Basic Babel Setup"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

class Config:
    """Config class for flask app
    """
    
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """view function for root route
    Returns:
        html: homepage
    """
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    """get best language match
    Returns:
        str: best match
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# babel.init_app(app, locale_selector=get_locale)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

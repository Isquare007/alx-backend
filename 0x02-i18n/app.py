#!/usr/bin/env python3
"""Basic Babel Setup"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
from pytz import timezone
from pytz.exceptions import UnknownTimeZoneError

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)


class Config(object):
    """Config class for flask app
    """

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def hello_world():
    """
    parametersize
    """
    g.time = format_datetime()
    return render_template("index.html")


@babel.localeselector
def get_locale():
    """get best language match
    Returns:
        str: best match
    """
    locale = request.args.get('locale', '')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user.get('locale')

    locale = request.headers.get('locale', '')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """gets user login"""
    user_id = request.args.get('login_as')

    if user_id:
        return users.get(int(user_id))
    return None


@babel.timezoneselector
def get_timezone():
    """
    Gets the timezone from the URL parameters, users settings and validate it
    and the default timezone
    """
    tz = request.args.get('timezone',  '').strip()
    if not tz and g.user:
        tz = g.user['timezone']
    try:
        timezone(tz)
    except UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.before_request
def before_request():
    """runs before any other function"""

    g.user = get_user()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)

#!/usr/bin/env python3
"""a flask app"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def welcome():
    """outputs “Welcome to Holberton” as page title"""
    message = "Welcome to Holberton", "Hello World"
    return render_template('0-index.html', title=message)

if __name__ == "__main__":
    """ Main Function """
    app.run()

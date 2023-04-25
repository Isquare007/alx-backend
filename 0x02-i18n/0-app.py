#!/usr/bin/env python3
"""a flask app"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def welcome():
    """outputs “Welcome to Holberton” as page title"""
    message = "Welcome to Holberton"
    return render_template('0-index.html', title=message)

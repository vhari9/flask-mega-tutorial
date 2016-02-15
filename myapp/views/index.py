# -*- coding: utf-8 -*-

from myapp import app
from flask import render_template

@app.route('/')
def index():
    user = {'nick': 'eggpuff'}
    posts = [
        {
            'author': {'nick': 'eggpuff'},
            'body': 'Beautiful day out here!'
        },
        {
            'author': {'nick': 'dimsum'},
            'body': 'om Nom NOM NOm'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
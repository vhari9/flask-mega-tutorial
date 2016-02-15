# -*- coding: utf-8 -*-

from .. import app, db, lastuser
from ..models import User, Post
from flask import render_template

@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@lastuser.requires_login
@app.route('/add', methods=['POST'])
def add_entry():
    # TODO: add code to add entry
    flash('New entry was successfully posted')
    return redirect(url_for('index'))

@lastuser.requires_login
# FIXME: This way we delete all posts that match the title!
@app.route('/delete/<path:title>', methods=['POST'])
def delete_entry(title):
    # TODO: add code to delete entry!
    flash('Entry was successfully deleted')
    return redirect(url_for('index'))
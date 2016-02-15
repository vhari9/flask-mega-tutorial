# -*- coding: utf-8 -*-

from ..models import User, Post, db
from .. import app, lastuser
from flask import render_template, g, flash, render_template, redirect, url_for,\
    request, session
from datetime import datetime

@app.route('/')
def index():
    if session['logged_in']:
        posts = Post.query.filter_by(user_id=g.user.id)
    else:
        posts = Post.query.all()
    return render_template('index.html', posts=posts)

@lastuser.requires_login
@app.route('/add', methods=['POST'])
def add():
    post = Post(body=request.form['body'], timestamp=datetime.utcnow(), author=g.user)
    db.session.add(post)
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('index'))

@lastuser.requires_login
# FIXME: This way we delete all posts that match the body text!
@app.route('/delete/<path:body>', methods=['POST'])
def delete(body):
    posts = Post.query.filter_by(body=body)
    for post in posts:
        db.session.delete(post)
    db.session.commit()
    flash('Entry was successfully deleted')
    return redirect(url_for('index'))
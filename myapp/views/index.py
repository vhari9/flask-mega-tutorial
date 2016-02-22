# -*- coding: utf-8 -*-

from ..models import User, Post, db
from .. import app, lastuser
from flask import render_template, g, flash, render_template, redirect, url_for,\
    request, session, message_flashed
from datetime import datetime
from flask.ext.sqlalchemy import get_debug_queries
from config import ProfileConfig
import logging

# @app.after_request
# def after_request(response):
#     for query in get_debug_queries():
#         if query.duration >= ProfileConfig.DATABASE_QUERY_TIMEOUT:
#             app.logger.warning("SLOW QUERY: %s\nParameters: %s\nDuration: %fs\nContext: %s\n" % (query.statement, query.parameters, query.duration, query.context))
#     return response

def log_request(sender, **params):
    logging.debug(params.items())

message_flashed.connect(log_request, app)

@app.route('/')
def index():
    posts = Post.query.all()
    if g.user:
        posts = Post.query.filter_by(user_id=g.user.id)
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
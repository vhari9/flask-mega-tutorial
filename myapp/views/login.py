# -*- coding: utf-8 -*-

from flask import Flask, redirect, session, request, abort, render_template, \
    flash, Markup, escape
from coaster.views import get_next_url
from baseframe import _
from baseframe.forms import render_message
from .. import app, lastuser
from ..models import db

@app.route('/login')
@lastuser.login_handler
def login():
    session['logged_in'] = True
    return {'scope':'id email/*'}

@app.route('/logout')
@lastuser.logout_handler
def logout():
    session['logged_in'] = False
    flash(_('You were logged out'), category='info')
    return get_next_url()

@app.route('/login/redirect')
@lastuser.auth_handler
def lastuserauth():
    db.session.commit()
    return redirect(get_next_url())

@app.route('/login/notify', methods=['POST'])
@lastuser.notification_handler
def lastusernotify(user):
    db.session.commit()

@lastuser.auth_error_handler
def lastuser_error(error, error_description=None, error_uri=None):
    if error == 'access_denied':
        flash(_(u"You denied the request to login"), category='error')
        return redirect(get_next_url())
    return render_message(
        title=_(u"Error: {error}").format(error=error),
        message=Markup(
            u"<p>{desc}</p><p>URI: {uri}</p>".format(
                desc=escape(error_description or u''), uri=escape(error_uri or _(u'NA')))
            )
    )

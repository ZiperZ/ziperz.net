from flask import session, flash, redirect, url_for, render_template
from datetime import datetime
from ziperz import db, pages

class Topic(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String(50), nullable=False, unique=True)
    address     = db.Column(db.String(50), nullable=False, unique=True)
    post_date   = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content     = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'{self.title}\n{self.post_date}\n{self.content}\n'

def title_to_address(title):
    print("TITLE==", title)
    address = ''
    for i in title:
        if i.isalpha():
            print(i)
            address = address.join(i)
        else:
            address = address.join('-')

    print("ADDERSS====", address)

    return address

""" Decorator function """
def root_account_required(f):
    def decorated_function(*args, **kwargs):
        if not 'root_logged' in session:
            flash('You must logged in if you wanna enter this page.', 'error')
            return redirect(url_for('root_login'))

        return f(*args, **kwargs)
    return decorated_function
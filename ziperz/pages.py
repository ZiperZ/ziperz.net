from flask import render_template, redirect, url_for, request, abort, flash, send_from_directory, session
from ziperz import app, db
from ziperz.classes import Topic, title_to_address, root_account_required
import os

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error404.html'), 404

@app.route('/favicon.ico')
def favicon():
    print('hello')
    return send_from_directory(app.root_path, 'favicon.ico', mimetype='favicon.ico')

@app.route('/')
def index():
    topics = Topic.query.all()
    return render_template('index.html', topics=topics)

@app.route('/topic/')
def list_topic():
    topics = Topic.query.order_by(Topic.post_date.desc()).limit(20).all()
    return render_template('list_topic.html', topics=topics)

@app.route('/topic/<string:address>')
def topic(address):
    topic = Topic.query.filter_by(address=address).first()

    if topic != None:
        return render_template('topic.html', topic=topic)
    else:
        abort(404)

@app.route('/create-topic', methods=['GET', 'POST'])
def create_topic():
    if request.method == 'POST':
        title   = request.form['title']
        content = request.form['content']
        address = title_to_address(title)

        topic = Topic(title=title, content=content, address=address)

        try:
            db.session.add(topic)
            db.session.commit()
        except:
            flash('FAILED TO CREATE TOPIC', 'error')
            return render_template('create_topic.html', title=title, content=content)
        else:
            flash('SUCCESSFULY CREATED TOPIC', 'success')
            return redirect(url_for('index'))
    else:
        return render_template('create_topic.html')

@app.route('/root')
@root_account_required
def root():
    src = url_for('static', filename='video/example.mp4')
    return render_template('video.html', video_source=src)

@app.route('/root-login', methods=['GET', 'POST'])
def root_login():
    if request.method == 'POST':
        session['root_logged'] = True

        flash('Successfully logged in!', 'success')
        return redirect(url_for('index'))
    else:
        return render_template('root_login.html')
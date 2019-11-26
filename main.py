from ziperz import db as database, app as application

if __name__ == '__main__':
    database.create_all()
    application.run(debug=True)
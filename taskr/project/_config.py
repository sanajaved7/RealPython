import os

#get folder where script lives

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
#for cross-site request forgery prevention (aka more security)
WTF_CSRF_ENABLED = True
#for managing user sessions
SECRET_KEY = "\xca\x07\xffB\x9a\xe3&\x89\xa5\xc2\xd8Z\xde}\x11\xaf5cG!\xf6'\xf5k"

#define full path for the DB
DATABASE_PATH = os.path.join(basedir, DATABASE)



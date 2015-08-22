import os
import unittest

from views import app, db
from _config import basedir
from models import User

TEST_DB = 'test.db'

class AllTests(unittest.TestCase):

    #setup and teardown

    #execute prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, TEST_DB)
        self.app = app.test_client()
        db.create_all()

    #execute after each test
    def tearDown(self):
        db.drop_all()

    #each test should start with 'test'
    def test_user_setup(self):
        new_user = User("sana", "sana@sana.com", "sanajaved")
        db.session.add(new_user)
        db.session.commit()
        test = db.session.query(User).all()
        for t in test:
            t.name
        assert t.name == "sana"

    #### Unit Test for Users ####

    #test that form is present on login page
    def test_form_is_present_on_login_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Please sign in to access your task list', response.data)

    #helper function to login
    def login(self, name, password):
        return self.app.post('/', data=dict(name=name, password=password), follow_redirects=True)

    #test that unregistered users cannot login
    def test_users_cannot_login_unless_registered(self):
        response = self.login('foo', 'bar')
        self.assertIn(b'Invalid username or password.', response.data)

    #helper method to register users
    def register(self, name, email, password, confirm):
        return self.app.post('register/', data=dict(name=name, email=email, password=password, confirm=confirm), follow_redirects=True)

    #test that registered users can login
    def test_users_can_login(self):
        self.register('Michael', 'michael@realpython.com', 'python', 'python')
        response = self.login('Michael', 'python')
        self.assertIn("Welcome!!!!", response.data)

    #testing bad data
    def test_invalid_form_data(self):
        self.register('Michael', 'michael@realpython.com', 'python', 'python')
        response = self.login('alert("alert box!");', 'foo')
        self.assertIn(b'Invalid username or password.', response.data)

    #tests if users can register
    def test_user_registration(self):
        self.app.get('register/', follow_redirects=True)
        response = self.register('Michael', 'michael@realpython.com', 'python', 'python')
        self.assertIn(b'Thanks for registering!!!! :D Please login.', response.data)

    def test_user_registration_error(self):
        self.app.get('register/', follow_redirects=True)
        self.register('Michael', 'michael@realpython.com', 'python', 'python')
        self.app.get('register/', follow_redirects=True)
        response = self.register('Michael', 'michael@realpython.com', 'python', 'python')
        self.assertIn(b'That username and/or email already exist', response.data)

    #helper method to log users out
    def logout(self):
        return self.app.get('logout/', follow_redirects=True)

    #test if users can logout
    def test_logged_in_users_can_logout(self):
        self.register('Fletcher', 'fletcher@realpython.com', 'python101', 'python101')
        self.login('Fletcher', 'python101')
        response = self.logout()
        self.assertIn(b'Goodbye!', response.data)

if __name__ == "__main__":
    unittest.main()

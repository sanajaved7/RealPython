from views import db
from models import Task
from datetime import date

#create db and the db table
db.create_all()

#insert data
db.session.add(Task("Finish this tutorial", date(2015,3,3), 10, 1))

db.session.add(Task("Finish Real Python", date(2015, 8, 15), 10, 1))

db.session.commit()

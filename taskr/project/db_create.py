import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:

    #get cursor object
    c = connection.cursor()

    #create the table
    c.execute("""CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, due_date TEXT NOT NULL, priority INTEGER NOT NULL, status INTEGER NOT NULL)""")

    #insert dummy data
    c.execute('INSERT INTO tasks(name, due_date, priority, status)' 'VALUES("Finish this tutorial", "08/04/2015", 10, 1)')
    c.execute(
        'INSERT INTO tasks(name, due_date, priority, status)'
        'VALUES("Finish Real Python", "08/04/2015", 10, 1)'
        )

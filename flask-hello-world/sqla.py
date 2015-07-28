#import sqlite
import sqlite3

#create new DB
conn = sqlite3.connect("new.db")

#get a cursor object to execute SQL commands
cursor = conn.cursor()

#create table
cursor.execute("""CREATE TABLE population (city TEXT, state TEXT, population INT)""")

#close DB connection
conn.close()

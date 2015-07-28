import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    #insert multiple records with tuples
    cities = [
    ('Boston', 'MA', 600000),
    ('Los Angeles', 'CA', 38000000),
    ('Houston', 'TX', 2100000),
    ('Philadelphia', 'PA', 1500000),
    ('San Antonio', 'TX', 1400000),
    ('San Diego', 'CA', 130000),
    ('Dallas', 'TX', 1200000),
    ('San Jose', 'CA', 900000),
    ('Jacksonville', 'FL', 800000),
    ('Indianapolis', 'IN', 800000),
    ('Austin', 'TX', 800000),
    ('Detroit', 'MI', 700000)
    ]

    #insert data into table
    c.executemany('INSERT into population VALUES(?, ?, ?)', cities)

    # #update data
    # c.execute("UPDATE population SET population = 9000000 WHERE city = 'New York City'")

    # #delete data
    # c.execute("DELETE FROM population WHERE city = 'Boston'")

    # print "\nNEW DATA:\n"

    c.execute("SELECT * FROM population WHERE population > 1000000")

    rows = c.fetchall()

    for r in rows:
        print r[0], r[1], r[2]

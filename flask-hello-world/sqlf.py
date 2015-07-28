import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    #JOINing data from multiple tables
    # c.execute("""SELECT DISTINCT population.city, population.population, regions.region FROM population, regions WHERE population.city = regions.city ORDER BY population.city ASC""")

    # rows = c.fetchall()

    # for r in rows:
    #     print "City: " + r[0]
    #     print "Population: " + str(r[1])
    #     print "Region: " + r[2]

    #create dictionary of SQL queries
    sql = {'average': "SELECT avg(population) FROM population",
        'maximum': "SELECT max(population) FROM population",
        'minimum': "SELECT min(population) FROM population",
        'sum': "SELECT sum(population) FROM population",
        'count': "SELECT count(city) FROM population"
        }

    #run each sql query item in the dictionary
    for keys, values in sql.iteritems():

        #run sql
        c.execute(values)

        #retrieves record from qury
        result = c.fetchone()

        #output results
        print keys + ":", result[0]

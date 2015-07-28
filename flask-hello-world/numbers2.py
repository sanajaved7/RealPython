import sqlite3
import random

with sqlite3.connect("newnum.db") as connection:

    c = connection.cursor()

    while True:
        userinput = raw_input("Please enter 1 to calculate the average number, 2 for the max number, 3 for the min number, 4 for the sum of the numbers, or 5 to exit the program: ")
        if userinput == "1":
            c.execute("SELECT avg(num) FROM numbers")
            result = c.fetchone()
            print "The average number is " + str(result[0])
        elif userinput == "2":
            c.execute("SELECT max(num) FROM numbers")
            result = c.fetchone()
            print "The max number is " + str(result[0])
        elif userinput == "3":
            c.execute("SELECT min(num) FROM numbers")
            result = c.fetchone()
            print "The min number is " + str(result[0])
        elif userinput == "4":
            c.execute("SELECT sum(num) FROM numbers")
            result = c.fetchone()
            print "The sum of numbers is " + str(result[0])
        elif userinput == "5":
            break

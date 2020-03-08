from sqlite3 import Error
import sqlite3

con = sqlite3.connect('mydatabase.db')


cursorObj = con.cursor()


def sql_connection():

    try:

        con = sqlite3.connect(':memory:')

        print("Connection is established: Database is created in memory")

    except Error:

        print(Error)

    finally:

        con.close()


sql_connection()

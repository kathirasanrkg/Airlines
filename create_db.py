import sqlite3 as sql

#connect to SQLite
con = sql.connect('db_airline.db') #CREATE DATABASE

#Create a Connection
cur = con.cursor()

#Drop users table if already exist.
cur.execute("DROP TABLE IF EXISTS airline")

#Create users table in db_AIR database
sql ='''CREATE TABLE airline (
    UID INTEGER PRIMARY KEY AUTOINCREMENT,
	FLIGHTNUMBER NUMBER,
	AIRLINE TEXT,
    DEPARTURECITY TEXT,
    ARRIVALCITY TEXT,
    DEPARTURETIME TIME,
    ARRIVALTIME TIME,
    STATUS TEXT
    )'''
cur.execute(sql)

#commit save changes
con.commit()

#close the connection
con.close()
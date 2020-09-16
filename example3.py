import sqlite3 as sql
import os

def clearfunc():
	os.system("clear" if os.name == "nt" "cls" else "clear")

clearfunc()


def connection_sql():

	database = str(input("Enter a Database : ") + ".db")
	conn = sql.connect(database)

	c = conn.cursor()

	customers = [("aylin","kaya"),
		("hande","kaya"),
		("buse","kaya")]
	c.execute("CREATE TABLE IF NOT EXISTS customer (ID INTEGER PRIMARY KEY,name TEXT,surname TEXT)")
	for veri in customers:
		c.execute("INSERT INTO customer (name,surname) VALUES (?,?)",veri)

	conn.commit()
	conn.close()

connection_sql()

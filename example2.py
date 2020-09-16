import sqlite3
import sys
import os


def systemclearfunc():
	os.system("clear" if os.name == "nt" "cls" else "clear")

systemclearfunc()

def sqlconnectionmy(dbnames):
	with sqlite3.connect(dbnames) as conn:
		c = conn.cursor()
		c.execute("""CREATE TABLE IF NOT EXISTS customers (ID INTEGER PRIMARY KEY, name TEXT , surname TEXT)""")
		c.execute("INSERT INTO customers (name,surname) values ('meryem','kaya')")
		c.execute("INSERT INTO customers (name,surname) values ('ebru','kaya')")
		c.execute("INSERT INTO customers (name,surname) values ('buse','kaya')")
		conn.commit()
		conn.close()

try:
	users = str(input("Create Database Name : "))
	print("Creating" + "\n" + users + ".db")
	sqlconnectionmy(users + ".db")

except Exception as e:
	print(e)
	sys.exit()

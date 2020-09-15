import sqlite3
import sys
import os


def systemclearfunc():
	os.system("clear" if os.name == "nt" "cls" else "clear")

systemclearfunc()

def sqlconnectionmy(dbnames):
	conn = sqlite3.connect(dbnames)
	c = conn.cursor()
	c.execute("""CREATE TABLE customers (ID INTEGER , name TEXT , surname TEXT)""")
	c.execute("INSERT INTO customers (ID,name,surname) values (1,'meryem','kaya')")
	c.execute("INSERT INTO customers (ID,name,surname) values (2,'ebru','kaya')")
	c.execute("INSERT INTO customers (ID,name,surname) values (3,'buse','kaya')")
	conn.commit()
	conn.close()

try:
	users = str(input("Create Database Name : "))
	sqlconnectionmy(users + ".db")

except Exception as e:
	print(e)
	sys.exit(0)
	

# Create a SQLite3 database and table

# import the sqlite3 library
import sqlite3




conn = sqlite3.connect("cars.db")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE inventory 
	              (make TEXT, model TEXT, quantity INT)
	           """)

conn.close()


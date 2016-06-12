import sqlite3

# executemany() method

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()
	
	# insert multiple records using a tuple
	cars = [
		('Ford', 'MA', 6),
		('Honda', 'IL', 27), 
		('Honda', 'TX', 21), 
		('Ford', 'AZ', 15),
		('Ford','CC',12)
		]
	
	# insert data into table
	c.executemany('INSERT INTO inventory VALUES(?, ?, ?)', cars)
import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	# update data
	c.execute("UPDATE inventory SET quantity = 11 WHERE model='MA'")
	c.execute("UPDATE inventory SET quantity = 22 WHERE model='TX'")

	print "\nNEW DATA:\n"

	c.execute("SELECT * FROM inventory")
	rows = c.fetchall()
	for r in rows:
		print r[0], r[1], r[2]
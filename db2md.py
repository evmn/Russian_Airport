import sqlite3
def db2md():
	conn = sqlite3.connect('RussianAirport.db')
	db = conn.cursor()
	print("|Airport|Latitude|Longitude|")
	print("|:-|:-:|:-:|")
	for airport in db.execute('select * from russian_airport').fetchall():
		print('|', airport[1], '|', airport[3], '|', airport[4], '|')
db2md()

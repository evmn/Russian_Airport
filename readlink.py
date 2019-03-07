from urllib.request import urlopen
import re, time, os, sys
from bs4 import BeautifulSoup
import sqlite3

def start_requests():
	conn = sqlite3.connect('RussianAirport.db')
	db = conn.cursor()
	db.execute('''
		create table if not exists russian_airport 
		(id integer primary key autoincrement,
		airport text, 
		wikipage text,
		latitude text,
		longitude text)''')
	with open('links', 'r') as f:  # read the list of urls
		for url in f.readlines():
			try:
				html = urlopen(url)
				bsObj = BeautifulSoup(html, "lxml")
				airport = bsObj.find('h1').get_text()
				wikipage = url
				latitude = bsObj.find('span', attrs={"class":"latitude"}).get_text()
				longitude = bsObj.find('span', attrs={"class":"longitude"}).get_text()
				print(airport)
				print(latitude)
			except:
				pass
			db.execute('''insert into russian_airport(airport, wikipage, latitude, longitude)
				values(?,?, ?, ?)
				''', (airport, wikipage, latitude, longitude))
			conn.commit()
		conn.close()

start_requests()

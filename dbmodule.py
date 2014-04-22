#!/usr/bin/python

import sqlite3 as lite
import sys

DB_NAME = "test.db"


def check_database():
	"""
	Checks to see if sqlite can properly connect to a database, if not, it creates the db file.	
	"""
	con = None

	try:
		con = lite.connect(DB_NAME)
	
		cur = con.cursor()    
		cur.execute('SELECT SQLITE_VERSION()')
	
		data = cur.fetchone()
	
		print "SQLite version: %s" % data                
	
	except lite.Error, e:
	
		print "Error %s:" % e.args[0]
		sys.exit(1)
	
	finally:
	
		if con:
			con.close()

def create_database_table():
	"""
	Creates the table in the database
	"""
	
	try:
		con = lite.connect(DB_NAME)
	
		with con:
			cur = con.cursor()    
			cur.execute("CREATE TABLE Site(Id INT, Url TEXT, Count INT)")
	
	except lite.Error, e:
	
		print "Error %s:" % e.args[0]
		sys.exit(1)
	
	finally:
	
		if con:
			con.close()
			
def insert_dummy_data():
	"""
	Creates the table in the database
	"""
	
	try:
		con = lite.connect(DB_NAME)
	
		with con:
			cur = con.cursor()    
			#cur.execute("CREATE TABLE Site(Id INT, Url TEXT, Count INT)")
			cur.execute("INSERT INTO Site VALUES(1,'http://cnn.com',-1)")
			cur.execute("INSERT INTO Site VALUES(2,'http://foxnews.com',-1)")
			cur.execute("INSERT INTO Site VALUES(3,'http://nbcnews.com',-1)")
			cur.execute("INSERT INTO Site VALUES(4,'http://espn.com',-1)")
	
	except lite.Error, e:
	
		print "Error %s:" % e.args[0]
		sys.exit(1)
	
	finally:
	
		if con:
			con.close()
			
			
def get_id_from_url(url):
	"""
	Returns the id of the provided website
	"""
	
	try:
		con = lite.connect(DB_NAME)
	
		with con:
			cur = con.cursor()
			cur.execute("SELECT id FROM Site WHERE url == '%s'" % url )	  
			row = cur.fetchone()
		
			if row == None:
				result = "-1"
			else:
				result = row[0]    
			
	
	except lite.Error, e:
	
		print "Error %s:" % e.args[0]
		sys.exit(1)
	
	finally:
	
		if con:
			con.close()
	return result
	
	
def update_site_count(url,new_count):
	"""
	Updates the count for a given website
	"""
	
	site_id = get_id_from_url(url)
	
	try:
		con = lite.connect(DB_NAME)
	
		with con:
			cur = con.cursor()	  
			cur.execute("UPDATE Site SET Count=? WHERE Id=?", (new_count, site_id)) 
	
	except lite.Error, e:
	
		print "Error %s:" % e.args[0]
		sys.exit(1)
	
	finally:
	
		if con:
			con.close()

def get_site_count(url):
	"""
	Returns the count of the provided website
	"""
	
	try:
		con = lite.connect(DB_NAME)
	
		with con:
			cur = con.cursor()
			cur.execute("SELECT Count FROM Site WHERE url == '%s'" % url )	  
			row = cur.fetchone()
		
			if row == None:
				result = "-1"
			else:
				result = row[0]    
			
	
	except lite.Error, e:
	
		print "Error %s:" % e.args[0]
		sys.exit(1)
	
	finally:
	
		if con:
			con.close()
	return result
			


# Main Method Stuff			
#check_database()
# create_database_table()
#insert_dummy_data()

#print get_id_from_url("http://foxnews2.com")

site = "http://cnn.com"
update_site_count(site,9999)
print get_site_count(site)
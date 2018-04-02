import sys
import random
import hashlib
import MySQLdb

def connect_db():
	HOST="localhost"
	USER="root"
	PASSWORD="B@dhorsie.123"
	DATABASE="HoneyWordDB"
	db=MySQLdb.connect(host=HOST,user=USER,passwd=PASSWORD,db=DATABASE)
	return db
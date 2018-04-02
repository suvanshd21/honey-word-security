import sys
import random
import hashlib
import MySQLdb

from .connectdb import connect_db

#Verifying entered password with honeywords
def honey_checker(username,password):
	db=connect_db()
	c=db.cursor()
	query="SELECT password_hash FROM Login WHERE username = '"+username+"'"
	c.execute(query)
	res=c.fetchone()
	hashed_pw=hashlib.sha256(password.encode("UTF-8")).hexdigest()
	flag=0
	for i in range(0,len(res[0]),64):
		if hashed_pw == res[0][i:i+64]:
			query="SELECT password_index FROM HoneyChecker WHERE username = '"+username+"'"
			c.execute(query)
			res2=c.fetchone()
			if i/64 == res2[0]:
				return "Correct"
			else:
				return "Intruder"
			flag=1
			break
	if flag ==0:
		return "Incorrect"
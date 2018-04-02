import sys
import random
import hashlib
import MySQLdb

from .connectdb import connect_db

#Parameters for generating honey words
class params:
	#Number of honey words generated per password
	n = 5 
	#Probability threshold according to which a character is tweaked
	tweak_prob = 0.5

#Honey Words Generation
def honeyword_gen(password):
	honeywords=[]
	for i in range(5):
		temp=[]
		for j in password:
			rand=random.randint(1,101)/100
			if(rand>0.7):
				if(j.isupper()):
					temp.append(j.lower())
				elif(j.islower()):
					temp.append(j.upper())
				elif(j.isdigit()):
					temp.append(str((int(j)+random.randint(1,11))%10))
				else:
					temp.append(j)
			else:
				temp.append(j)
		if temp not in honeywords:
			honeywords.append(''.join(temp))
		else:
			i-=1
	return honeywords

#Sweet Word String Generation
def sweetstring_gen(passwords):
	honeywords=[]
	if type(passwords) is str:
		passwords=passwords.split(" ")
	for password in passwords:
		tmp_honeywords=honeyword_gen(password)
		for tmp_honeyword in tmp_honeywords:
			honeywords.append(tmp_honeyword)
	sweetwords=honeywords+passwords
	random.shuffle(sweetwords)
	print("Generated sweetwords are: ",sweetwords)
	pw_index=sweetwords.index(password)
	hashed_sweetwords=''
	for sweetword in sweetwords:
		m=hashlib.sha256(sweetword.encode("UTF-8")).hexdigest()
		hashed_sweetwords+=m
	return pw_index,hashed_sweetwords


#Storing Sweet String in database
def store_db(u,h,i):
	db=connect_db()
	if db is None:
		print("Can't connect.")
		return
	c=db.cursor()
	query = "INSERT INTO Login VALUES('"+u+"','"+h+"')"
	c.execute(query)
	query = "INSERT INTO HoneyChecker VALUES('"+u+"','"+str(i)+"')"
	c.execute(query)
	db.commit()

#main function
def store_sweet_string(username,password):
	pw_index,hashed_sweetwords=sweetstring_gen(password)
	store_db(username,hashed_sweetwords,pw_index)


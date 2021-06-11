import mysql.connector
from xpxchain import models
import hashlib
import time
import gc

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sharmelen",
  database="e_vote"
)

mycursor = mydb.cursor()


account = models.Account.generate_new_account(models.NetworkType.TEST_NET)

pub_key = str(account.public_key)
priv_key = str(account.public_key)

hash_priv_key = hashlib.sha256(priv_key.encode())
hashed_priv_key = str(hash_priv_key.hexdigest())

sql = "INSERT INTO admin_cred (pub_key, priv_hash_key, priv_key) VALUES (%s, %s, %s)"
val = (pub_key, hashed_priv_key, priv_key)
mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "record inserted.")

gc.collect()

	
	
	
# for x in range (40):

	
	
	# stud_name = "STUDENT_"+str(x)
	
	# int_no = 10000+x
	# mt_no = str(int_no)
	
	# sql =  "INSERT INTO faculty_seat (name, mt_no) VALUES (%s, %s)"
	# val = (stud_name, mt_no)
	
	# mycursor.execute(sql, val)
	# mydb.commit()
	
	# print(mycursor.rowcount, "record inserted.")






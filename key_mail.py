import smtplib, ssl
import mysql.connector
import hashlib
from xpxchain import models


mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  password="sharmelen",
	  database="trial_two"
	)

mycursor = mydb.cursor()

def mail(email_id,faculty):
	
	account = models.Account.generate_new_account(models.NetworkType.MIJIN_TEST)

	print(account.public_key)
	print(account.private_key)
	
	
	
	port = 465  # For SSL
	smtp_server = "smtp.gmail.com"
	sender_email = "sharmelenvasnthan@gmail.com"  # Enter your address
	receiver_email = email_id                           ##"sharmelenvasanthan@gmail.com"  # Enter receiver address
	password = "yourpass"
	msg =  "Your Private Key Is: " + str(account.private_key) + "\nYour Public Key Is: " +  (account.public_key)                                         ##"OMG IT WORKS!!!!!!!"
	message = """\
	Subject: Vote Key

	%s""" % msg


	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, message)
	
	print("email sent")
	
	hash_priv_key = hashlib.sha256((account.private_key).encode())
	hashed_priv_key = str(hash_priv_key.hexdigest())
	
	sql = "INSERT INTO name (pub_key,priv_key_hash,public_status,faculty_status,faculty,priv_key) VALUES ('"+str(account.public_key)+"','"+hashed_priv_key+"','not voted','not voted','"+faculty+"','"+str(account.private_key)+"')"
	
	mycursor.execute(sql)
	mydb.commit()
	
	print("Inserted in Database")
	
		
sql = "SELECT * FROM email_add"
mycursor.execute(sql)
result = mycursor.fetchall()

for x in range (len(result)):
	print(result[x][0])
	print(result[x][1])
	
	mail(result[x][0],result[x][1])


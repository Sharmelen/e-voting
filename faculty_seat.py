import wx
import mysql.connector
from collections import Counter
import matplotlib.pyplot as plt
import operator
import numpy as np

def faculty_winners(faculty):
	print("Hello")

	mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  password="sharmelen",
	  database="e_vote"
	)

	mycursor = mydb.cursor()

	sql = "SELECT name FROM faculty_seat_vote WHERE faculty = '"+faculty+"'"

	mycursor.execute(sql)
	result = mycursor.fetchall()

	names = []

	for x in range (len(result)):
		name = str(result[x]).strip("(',)")
		names.append(name)
		
	#print(names)

	names_dict = dict(Counter(names))

	#print(type(names_dict))
	high_vote = sorted(names_dict.items(),key=operator.itemgetter(1),reverse=True)

	high_name = []
	high_num = []

	for x in range (3):
		strip_brac = str(high_vote[x]).strip("()")
		split_vote = strip_brac.split(",")
		high_name.append(str(split_vote[0]).strip("''"))
		high_num.append(split_vote[1])
		
	high_name.reverse()
	high_num.reverse()

	x = np.array(high_name)
	y = np.array(high_num)

	f = open(str(faculty)+"_seat_winners.txt","w+")

	rev_name = high_name.reverse()

	pos_1 = high_name[0]+"- Head of MPP"
	pos_2 = high_name[1]+"- Assistant"
	pos_3 = high_name[2]+"- Secretary"


	f.write(pos_1+"\n"+pos_2+"\n"+pos_3)
	f.close()

	def addlabels(x,y):
		for i in range(len(x)):
			plt.text(i, y[i], y[i], ha = 'center')
			
	addlabels(x,y)
	

	plt.bar(x,y, color = "hotpink")
	plt.ylim(bottom=0)
	plt.show() 


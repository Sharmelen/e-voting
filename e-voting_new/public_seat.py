import wx
import mysql.connector
from collections import Counter
import matplotlib.pyplot as plt
import operator
import numpy as np


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sharmelen",
  database="e_vote"
)

mycursor = mydb.cursor()

sql = "SELECT name FROM public_seat_vote"

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

for x in range (6):
	strip_brac = str(high_vote[x]).strip("()")
	split_vote = strip_brac.split(",")
	high_name.append(str(split_vote[0]).strip("''"))
	high_num.append(split_vote[1])
	
high_name.reverse()
high_num.reverse()

x = np.array(high_name)
y = np.array(high_num)


plt.bar(x,y, color = "hotpink")
plt.ylim(bottom=0)
plt.show() 


# labels = []
# sizes = []

# for x, y in names_dict.items():
    # labels.append(x)
    # sizes.append(y)

# # Plot
# plt.pie(sizes, labels=labels)

# plt.axis('equal')
# plt.show()
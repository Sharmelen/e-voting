import wx
import mysql.connector
from vote_bc import *
import hashlib
import sys
from voting_panel_1 import *

def public_seat(private_key, stud_faculty):

	f = open("vote_result.txt","w")
	f.write("vote_result.txt","w")
	f.close()

	mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  password="sharmelen",
	  database="e_vote"
	)
	mycursor = mydb.cursor()

	sql = "SELECT name FROM public_seat"
	mycursor.execute(sql)
		
	result = mycursor.fetchall()
	names = []
		
	try:
		for x in range (len(result)):
			name = str(result[x][0])#.strip("(',)")
			names.append(name)
			
		#print(names)
		
	except:
		print("something went wrong")
		



	app = wx.App()
	win = wx.Frame(None, title="Voting Panel", size=(410, 350))
	win.SetBackgroundColour('white')

	vbox = wx.GridBagSizer(0,0)
	font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
	font.SetPointSize(9)

	def onChecked(event):
		cb = event.GetEventObject()
		
		result = str(cb.GetLabel())+'---'+str(cb.GetValue())+'\n'
		f = open("vote_result.txt","a")
		f.write(result)
		f.close()
			
			
		

	def submit_button(event):
		
		f = open("vote_result.txt","r")
		
		true_vote = []
		false_vote = []
		only_names = []
		
		for x in f:
		
			if "True" in x:
				true_vote.append(x)
				
			else:
				false_vote.append(x)
				
		#print(true_vote)
				
		for x in range (len(false_vote)):
			single_vote = false_vote[x]
			cand_name = single_vote.split("---")
			
			for y in range (len(true_vote)):
				single_true_vote = true_vote[y]
				#print(single_true_vote)
				if cand_name[0] in single_true_vote:
					#print(cand_name[0])
					true_vote.pop(true_vote.index(single_true_vote))
					
					break	
			
			
		if len(true_vote) == 6:
		
			private_key_vote = private_key
			hash_priv_key = hashlib.sha256(private_key_vote.encode())
			hashed_priv_key = str(hash_priv_key.hexdigest()) 
			
			sql_status = "SELECT public_status FROM key_table WHERE priv_key_hash = '"+str(hashed_priv_key)+"'"
			mycursor.execute(sql_status)
			status_result = mycursor.fetchall()
			
			if "not " in str(status_result):
		
				for j in range (len(true_vote)):
					final_name = true_vote[j].split("---")
					print(final_name[0])
					
					only_names.append(str(final_name[0]))
					
					sql = "INSERT INTO public_seat_vote (name) VALUES ('"+final_name[0]+"')"
					
					mycursor.execute(sql)
					mydb.commit()
					
					
					
					print("INSERTED!!")
					
				stud_private_key = private_key
				#bc_vote(stud_private_key, str(only_names))
				
				hash_priv_key = hashlib.sha256(stud_private_key.encode())
				hashed_priv_key = str(hash_priv_key.hexdigest())
				
				sql_update = "UPDATE key_table SET public_status = 'voted' WHERE priv_key_hash ='"+str(hashed_priv_key)+"'"
				mycursor.execute(sql_update)
				mydb.commit()
				
				print("DATA HAS BEEN UPDATED")
				
				faculty_stud = stud_faculty	
				faculty_seat(faculty_stud, stud_private_key)
				
				f = open("vote_result.txt","w")
				f.write("vote_result.txt","w")
				f.close()
				
				try:
					os.remove("vote_result.txt")
				except:
					print()
					
				sys.exit()
				
			else:
			
				try:
					os.remove("vote_result_1.txt")
				except:
					print()
					
				print("IT SEEMS THAT YOU HAVE VOTED")
				sys.exit()
			
				
				
		
		else:
			print(len(true_vote))
			print(true_vote)
			print("please pick 6 candidates")
			

	#######################################################################################################################

	title = wx.StaticText(win, label="Public Seat")
	title.SetFont(font)

	vbox.Add(title, pos = (0,7),flag=wx.ALL, border=5)
	######################################################################################################################

	check_1 = wx.CheckBox(win, label=names[0])
	check_1.Bind(wx.EVT_CHECKBOX, onChecked) 
	check_1.SetFont(font)
	vbox.Add(check_1, pos = (1,0),flag = wx.ALL, border = 5)

	######################################################################################################################

	check_2 = wx.CheckBox(win, label=names[1])
	check_2.Bind(wx.EVT_CHECKBOX, onChecked) 
	check_2.SetFont(font)
	vbox.Add(check_2, pos = (1,8),flag = wx.ALL, border = 10)

	######################################################################################################################

	check_3 = wx.CheckBox(win, label=names[2])
	check_3.Bind(wx.EVT_CHECKBOX, onChecked) 
	check_3.SetFont(font)
	vbox.Add(check_3, pos = (2,0),flag = wx.ALL, border = 5)

	######################################################################################################################

	check_4 = wx.CheckBox(win, label=names[3])
	check_4.Bind(wx.EVT_CHECKBOX, onChecked) 
	check_4.SetFont(font)
	vbox.Add(check_4, pos = (2,8),flag = wx.ALL, border = 10)

	######################################################################################################################

	check_5 = wx.CheckBox(win, label=names[4])
	check_5.Bind(wx.EVT_CHECKBOX, onChecked) 
	check_5.SetFont(font)
	vbox.Add(check_5, pos = (3,0),flag = wx.ALL, border = 5)

	######################################################################################################################

	check_6 = wx.CheckBox(win, label=names[5])
	check_6.Bind(wx.EVT_CHECKBOX, onChecked) 
	check_6.SetFont(font)
	vbox.Add(check_6, pos = (3,8),flag = wx.ALL, border = 10)

	######################################################################################################################

	check_7 = wx.CheckBox(win, label=names[6])
	check_7.Bind(wx.EVT_CHECKBOX, onChecked) 
	check_7.SetFont(font)
	vbox.Add(check_7, pos = (4,0),flag = wx.ALL, border = 5)

	######################################################################################################################

	check_8 = wx.CheckBox(win, label=names[7])
	check_8.Bind(wx.EVT_CHECKBOX, onChecked) 
	check_8.SetFont(font)
	vbox.Add(check_8, pos = (4,8),flag = wx.ALL, border = 10)

	######################################################################################################################

	check_9 = wx.CheckBox(win, label=names[8])
	check_9.Bind(wx.EVT_CHECKBOX, onChecked) 
	check_9.SetFont(font)
	vbox.Add(check_9, pos = (5,0),flag = wx.ALL, border = 5)

	######################################################################################################################

	check_10 = wx.CheckBox(win, label=names[9])
	check_10.Bind(wx.EVT_CHECKBOX, onChecked) 
	check_10.SetFont(font)
	vbox.Add(check_10, pos = (5,8),flag = wx.ALL, border = 10)

	######################################################################################################################

	check_11 = wx.CheckBox(win, label=names[10])
	check_11.Bind(wx.EVT_CHECKBOX, onChecked) 
	check_11.SetFont(font)
	vbox.Add(check_11, pos = (6,0),flag = wx.ALL, border = 5)

	######################################################################################################################

	check_12 = wx.CheckBox(win, label=names[11])
	check_12.Bind(wx.EVT_CHECKBOX, onChecked) 
	check_12.SetFont(font)
	vbox.Add(check_12, pos = (6,8),flag = wx.ALL, border = 10)


	######################################################################################################################
	btn_submit = wx.Button(win, label = 'Submit')
	btn_submit.Bind(wx.EVT_BUTTON, submit_button)
	vbox.Add(btn_submit, pos = (7,7),flag = wx.ALL, border = 10)

	win.SetSizerAndFit(vbox)
	win.Show()
	app.MainLoop()
	win.SetSizer(vbox)
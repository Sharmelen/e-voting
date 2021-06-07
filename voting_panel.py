import wx
import mysql.connector


#def public_seat():

app = wx.App()
win = wx.Frame(None, title="Voting Panel", size=(410, 350))
win.SetBackgroundColour('white')

vbox = wx.GridBagSizer(0,0)
font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
font.SetPointSize(9)

def onChecked(event):
	cb = event.GetEventObject()
	
	result = '\n'+str(cb.GetLabel())+'---'+str(cb.GetValue())+'\n'
	f = open("vote_result.txt","a")
	f.write(result)
	f.close()
		
		
	

def submit_button(event):
	
	f = open("vote_result.txt","r")
	
	true_vote = []
	false_vote = []
	
	for x in f:
	
		if "True" in x:
			true_vote.append(x)
			
		else:
			false_vote.append(x)
			
	print(len(true_vote))
			
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
		
		
				
	print(len(true_vote))
		
	
	
	

#######################################################################################################################

title = wx.StaticText(win, label="Public Seat")
title.SetFont(font)

vbox.Add(title, pos = (0,7),flag=wx.ALL, border=5)
######################################################################################################################

check_1 = wx.CheckBox(win, label="NAME_1")
check_1.Bind(wx.EVT_CHECKBOX, onChecked) 
check_1.SetFont(font)
vbox.Add(check_1, pos = (1,0),flag = wx.ALL, border = 5)

######################################################################################################################

check_2 = wx.CheckBox(win, label="NAME_2")
check_2.Bind(wx.EVT_CHECKBOX, onChecked) 
check_2.SetFont(font)
vbox.Add(check_2, pos = (1,8),flag = wx.ALL, border = 10)

######################################################################################################################

check_3 = wx.CheckBox(win, label="NAME_3")
check_3.Bind(wx.EVT_CHECKBOX, onChecked) 
check_3.SetFont(font)
vbox.Add(check_3, pos = (2,0),flag = wx.ALL, border = 5)

######################################################################################################################

check_4 = wx.CheckBox(win, label="NAME_4")
check_4.Bind(wx.EVT_CHECKBOX, onChecked) 
check_4.SetFont(font)
vbox.Add(check_4, pos = (2,8),flag = wx.ALL, border = 10)

######################################################################################################################

check_5 = wx.CheckBox(win, label="NAME_5")
check_5.Bind(wx.EVT_CHECKBOX, onChecked) 
check_5.SetFont(font)
vbox.Add(check_5, pos = (3,0),flag = wx.ALL, border = 5)

######################################################################################################################

check_6 = wx.CheckBox(win, label="NAME_6")
check_6.Bind(wx.EVT_CHECKBOX, onChecked) 
check_6.SetFont(font)
vbox.Add(check_6, pos = (3,8),flag = wx.ALL, border = 10)

######################################################################################################################

check_7 = wx.CheckBox(win, label="NAME_7")
check_7.Bind(wx.EVT_CHECKBOX, onChecked) 
check_7.SetFont(font)
vbox.Add(check_7, pos = (4,0),flag = wx.ALL, border = 5)

######################################################################################################################

check_8 = wx.CheckBox(win, label="NAME_8")
check_8.Bind(wx.EVT_CHECKBOX, onChecked) 
check_8.SetFont(font)
vbox.Add(check_8, pos = (4,8),flag = wx.ALL, border = 10)

######################################################################################################################

check_9 = wx.CheckBox(win, label="NAME_9")
check_9.Bind(wx.EVT_CHECKBOX, onChecked) 
check_9.SetFont(font)
vbox.Add(check_9, pos = (5,0),flag = wx.ALL, border = 5)

######################################################################################################################

check_10 = wx.CheckBox(win, label="NAME_10")
check_10.Bind(wx.EVT_CHECKBOX, onChecked) 
check_10.SetFont(font)
vbox.Add(check_10, pos = (5,8),flag = wx.ALL, border = 10)

######################################################################################################################

check_11 = wx.CheckBox(win, label="NAME_11")
check_11.Bind(wx.EVT_CHECKBOX, onChecked) 
check_11.SetFont(font)
vbox.Add(check_11, pos = (6,0),flag = wx.ALL, border = 5)

######################################################################################################################

check_12 = wx.CheckBox(win, label="NAME_12")
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
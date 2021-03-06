import wx
import socket
import sys
import hashlib
import mysql.connector
from voting_panel import *
import os

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sharmelen",
  database="e_vote"
)

mycursor = mydb.cursor()

app = wx.App()
win = wx.Frame(None, title="Login", size=(410, 150))
win.SetBackgroundColour('white')

vbox = wx.BoxSizer(wx.VERTICAL)
font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
font.SetPointSize(9)
##############################################################################################################
	
def account_info(event):
	
	priv_key = input_text1.GetValue()
	
	hash_priv_key = hashlib.sha256(priv_key.encode())
	hashed_priv_key = str(hash_priv_key.hexdigest())
	
	
	sql = "SELECT pub_key FROM admin_cred WHERE priv_hash_key = '"+str(hashed_priv_key)+"'"
	mycursor.execute(sql)
	
	result = mycursor.fetchall()
	
	try:
		print(str(result[0]).strip("(',)"))
		stud_faculty = str(result[0]).strip("(',)")
		
		os.system('python admin_selection.py')
	except:
		wx.MessageBox('Incorrect Login Credentials Please Try Again', 'ERROR',wx.OK | wx.ICON_ERROR)
	
	

##############################################################################################################
hbox1 = wx.BoxSizer(wx.HORIZONTAL)
st1 = wx.StaticText(win, label = "Private Key: ")

st1.SetFont(font)
hbox1.Add(st1, flag = wx.RIGHT, border = 8)


input_text1 = wx.TextCtrl(win, value = "")
hbox1.Add(input_text1, proportion = 1)

vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
##############################################################################################################

vbox.Add((-1,20))

hbox2 = wx.BoxSizer(wx.HORIZONTAL)

acc_info = wx.Button(win, label = 'Get Result', size = (150,30))
hbox2.Add(acc_info)
acc_info.Bind(wx.EVT_BUTTON, account_info)
vbox.Add(hbox2, flag = wx.CENTER)

win.SetSizer(vbox)

win.Show()
app.MainLoop()
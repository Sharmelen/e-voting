import wx
import os
from faculty_seat import *

def public_seat(event):
	print("You Pressed First")
	os.system('python public_seat.py')
	
def fppp_seat(event):
	print("You Pressed Second")
	#os.system('python account_information.py')
	faculty_winners("FPPP")
	
def fstp_seat(event):
	print("You Pressed Third")
	#os.system('python transaction.py')
	faculty_winners("FSTP")
	
def fpkp_seat(event):
	print("You Pressed Fourth")
	#os.system('python mosaic_tranx.py')
	faculty_winners("FPKP")
	
def fkj_seat(event):
	print("You Pressed Fifth")
	#os.system('python tranx_info.py')
	faculty_winners("FKJ")
	
def pb_seat(event):
	print("You Pressed Sixth")
	#os.system('python mosaic_null.py')
	faculty_winners("PB")
	
app = wx.App()
win = wx.Frame(None, title="Vote Result", size=(410, 200))
win.SetBackgroundColour('white')

vbox = wx.BoxSizer(wx.VERTICAL)

################################################################################
hbox1 = wx.BoxSizer(wx.HORIZONTAL)

gen_acc =  wx.Button(win, label = 'Public Seat', size = (150,30))
hbox1.Add(gen_acc)
gen_acc.Bind(wx.EVT_BUTTON, public_seat)

acc_info = wx.Button(win, label = 'FPPP Seat', size = (150,30))
hbox1.Add(acc_info, flag = wx.LEFT, border = 10)
acc_info.Bind(wx.EVT_BUTTON, fppp_seat)

vbox.Add(hbox1, flag = wx.CENTER, border=10)

################################################################################

vbox.Add((-1,20))

hbox2 = wx.BoxSizer(wx.HORIZONTAL)

make_tx = wx.Button(win, label = 'FSTP Seat',size = (150,30))
hbox2.Add(make_tx)
make_tx.Bind(wx.EVT_BUTTON, fstp_seat)

tx_info = wx.Button(win, label = 'FPKP Seat', size = (150, 30))
hbox2.Add(tx_info, flag = wx.LEFT, border = 10)
tx_info.Bind(wx.EVT_BUTTON, fpkp_seat)

vbox.Add(hbox2, flag = wx.CENTER, border = 10)

################################################################################

vbox.Add((-1,20))

hbox3 = wx.BoxSizer(wx.HORIZONTAL)

transaction_info = wx.Button(win, label = 'FKJ Seat', size = (150,30))
hbox3.Add(transaction_info)
transaction_info.Bind(wx.EVT_BUTTON, fkj_seat)

mosaic_cancel = wx.Button(win, label = 'PB Seat', size = (150, 30))
hbox3.Add(mosaic_cancel, flag = wx.LEFT, border = 10)
mosaic_cancel.Bind(wx.EVT_BUTTON, pb_seat)

vbox.Add(hbox3, flag = wx.CENTER)

###################################################################################

vbox.Add((-1,20))
hbox4 = wx.BoxSizer(wx.HORIZONTAL)

transaction_info = wx.Button(win, label = 'Vote Receipt', size = (150,30))
hbox4.Add(transaction_info)
#transaction_info.Bind(wx.EVT_BUTTON, fkj_seat)
vbox.Add(hbox4, flag = wx.CENTER)

win.SetSizer(vbox)

win.Show()

app.MainLoop()
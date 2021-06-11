import wx
import os

def public_seat(event):
	print("You Pressed First")
	os.system('python public_seat.py')
	
def fppp_seat(event):
	print("You Pressed Second")
	#os.system('python account_information.py')
	
def fstp_seat(event):
	print("You Pressed Third")
	#os.system('python transaction.py')
	
def fpkp_seat(event):
	print("You Pressed Fourth")
	#os.system('python mosaic_tranx.py')
	
def fkj_seat(event):
	print("You Pressed Fifth")
	#os.system('python tranx_info.py')
	
def pb_seat(event):
	print("You Pressed Sixth")
	#os.system('python mosaic_null.py')

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


win.SetSizer(vbox)

win.Show()

app.MainLoop()
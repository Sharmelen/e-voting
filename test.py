# import matplotlib.pyplot as plt

# your_data = {'DATE': 65,
 # 'ORG': 93,
 # 'PERSON': 62,
 # 'GPE': 18,
 # 'PRODUCT': 18,
 # 'FAC': 4,
 # 'CARDINAL': 50,
 # 'ORDINAL': 15,
 # 'NORP': 10,
 # 'MONEY': 3,
 # 'PERCENT': 2,
 # 'TIME': 5,
 # 'LOC': 5,
 # 'QUANTITY': 2}

# # Data to plot
# labels = []
# sizes = []

# for x, y in your_data.items():
    # labels.append(x)
    # sizes.append(y)

# # Plot
# plt.pie(sizes, labels=labels)

# plt.axis('equal')
# plt.show()



# import wx  
 
# class Example(wx.Frame): 
            
   # def __init__(self, parent, title): 
      # super(Example, self).__init__(parent, title = title,size = (200,200)) 
         
      # self.InitUI() 
		
   # def InitUI(self):    
             
      # pnl = wx.Panel(self) 
		  
      # self.cb1 = wx.CheckBox(pnl, label = 'Value A',pos = (10,10)) 
      # self.cb2 = wx.CheckBox(pnl, label = 'Value B',pos = (10,40)) 
      # self.cb3 = wx.CheckBox(pnl, label = 'Value C',pos = (10,70)) 
		
      # self.Bind(wx.EVT_CHECKBOX,self.onChecked) 
      # self.Centre() 
      # self.Show(True) 
      
   # def onChecked(self, e): 
      # cb = e.GetEventObject() 
      # print (cb.GetLabel(),' is clicked',cb.GetValue())
		
# ex = wx.App() 
# Example(None,'CheckBox') 
# ex.MainLoop()

# import wx

# app = wx.App()
# win = wx.Frame(None, title="Voting Panel", size=(410, 350))
# win.SetBackgroundColour('white')

# vbox = wx.GridBagSizer(0,0)
# font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
# font.SetPointSize(9)


# #######################################################################################################################

# title = wx.StaticText(win, label="Public Seat")
# title.SetFont(font)

# vbox.Add(title, pos = (0,7),flag=wx.ALL, border=5)
# ######################################################################################################################

# check_1 = wx.CheckBox(win, label="NAME_1")
# check_1.SetFont(font)
# vbox.Add(check_1, pos = (1,0),flag = wx.ALL, border = 5)

# ######################################################################################################################

# check_2 = wx.CheckBox(win, label="NAME_2")
# check_2.SetFont(font)
# vbox.Add(check_2, pos = (1,8),flag = wx.ALL, border = 10)

# ######################################################################################################################

# check_3 = wx.CheckBox(win, label="NAME_3")
# check_3.SetFont(font)
# vbox.Add(check_3, pos = (2,0),flag = wx.ALL, border = 5)

# ######################################################################################################################

# check_4 = wx.CheckBox(win, label="NAME_4")
# check_4.SetFont(font)
# vbox.Add(check_4, pos = (2,8),flag = wx.ALL, border = 10)

# ######################################################################################################################

# check_5 = wx.CheckBox(win, label="NAME_5")
# check_5.SetFont(font)
# vbox.Add(check_5, pos = (3,0),flag = wx.ALL, border = 5)

# ######################################################################################################################

# check_6 = wx.CheckBox(win, label="NAME_6")
# check_6.SetFont(font)
# vbox.Add(check_6, pos = (3,8),flag = wx.ALL, border = 10)

# ######################################################################################################################

# check_7 = wx.CheckBox(win, label="NAME_7")
# check_7.SetFont(font)
# vbox.Add(check_7, pos = (4,0),flag = wx.ALL, border = 5)

# ######################################################################################################################

# check_8 = wx.CheckBox(win, label="NAME_8")
# check_8.SetFont(font)
# vbox.Add(check_8, pos = (4,8),flag = wx.ALL, border = 10)

# ######################################################################################################################

# check_9 = wx.CheckBox(win, label="NAME_9")
# check_9.SetFont(font)
# vbox.Add(check_9, pos = (5,0),flag = wx.ALL, border = 5)

# ######################################################################################################################

# check_10 = wx.CheckBox(win, label="NAME_10")
# check_10.SetFont(font)
# vbox.Add(check_10, pos = (5,8),flag = wx.ALL, border = 10)

# ######################################################################################################################

# check_11 = wx.CheckBox(win, label="NAME_11")
# check_11.SetFont(font)
# vbox.Add(check_11, pos = (6,0),flag = wx.ALL, border = 5)

# ######################################################################################################################

# check_12 = wx.CheckBox(win, label="NAME_12")
# check_12.SetFont(font)
# vbox.Add(check_12, pos = (6,8),flag = wx.ALL, border = 10)


# ######################################################################################################################
# acc_info = wx.Button(win, label = 'Submit')
# #acc_info.Bind(wx.EVT_BUTTON, account_info)
# vbox.Add(acc_info, pos = (7,7),flag = wx.ALL, border = 10)

# win.SetSizer(vbox)
# win.Show()
# app.MainLoop()
# win.SetSizer(vbox)
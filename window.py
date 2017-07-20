import wx; 


class myva(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None,
		pos= wx.DefaultPosition, size=wx.Size(450, 100),
		style=MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN, 
		title="HereToHelp")
		
		panel= wx.Panel(self)
		mySizer= wx.BoxSizer(wx.VERTICAL)
		lbl= wx.StaticText(panel, label="HElloo")
		mySizer.Add(lbl, 0, wx.ALL, 5)
		self.txt= wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(400,30))
		self.txt.SetFocus()
		self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
		mySizer.Add(self.txt, 0, wx.ALL, 5)
		panel.SetSizer(mySizer)
		self.Show()
		
	def OnEnter(self, event):
		input= self.txt.GetValue()
		input.input.lower()
		print ("Done")
			
if __name__ == "__main__":
	app=wx.App(True)
	frame= myva()
	app.MainLoop()
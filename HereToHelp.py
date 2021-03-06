import wx; 
from espeak import espeak;
import speech_recognition as sr
import wolframalpha
import wikipedia


espeak.synth("Welcome")
class myva(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None,
		pos= wx.DefaultPosition, size=wx.Size(450, 100),
		style=MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN, 
		title="HereToHelp. How may I help you?")
		
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
		if input='':
			r = sr.Recognizer()
			with sr.Microphone() as source:
				audio = r.listen(source)
			try:
				self.txt.SetValue(r.recognize_google(audio))
			except sr.UnknownValueError:
				print("Google Speech Recognition could not understand audio")
			except sr.RequestError as e:
				print("Could not request results from Google Speech Recognition service; {0}".format(e))
		try:
		#wolframalpha
		app_id= "Put your own app ID"
		client= wolframalpha.Client(app_id)
		output= client.query(question)
		ans = next(output.results).text
		print(ans)
		espeak.synth("The answer is "+ans)
		
	except:
		input.split(' ')
		input= " ".join(input[2:])
		espeak.synth("Result for the " +input)
		print(wikipedia.summary(question))
			
if __name__ == "__main__":
	app=wx.App(True)
	frame= myva()
	app.MainLoop()

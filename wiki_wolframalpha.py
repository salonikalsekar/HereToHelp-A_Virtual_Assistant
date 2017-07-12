import wolframalpha
import wikipedia

while True:
	question= input("How may I help you? ")
	try:
		#wolframalpha
		app_id= "P3VHJY-W95YUQL25A"
		client= wolframalpha.Client(app_id)
		output= client.query(question)
		ans = next(output.results).text
		print(ans)
		
	except:
		print(wikipedia.summary(question))
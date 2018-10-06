from pyfiglet import figlet_format
from termcolor import colored
import requests

topic=input("\nlet me tell you a joke! give me a topic : ")
def jokes(topic):
	#data gathering
	url = "https://icanhazdadjoke.com/search"
	response = requests.get(url, 
		headers={"Accept":"application/json"},
		params={"term":"cat","limit":"1"}
		)
	data=response.json()
	#end
	return data
def bannerel(text,clr,on_clr,att1):
	#welcome banner
	asci_text=figlet_format(text1)
	clr_ascii_text=colored(asci_text, color=clr,on_color=on_clr, attrs=att1)
	#end
def 
	Print(f"\nI have {} jokes on {}".format(data["total_jokes"],data["search_term"]))

jokes("cat")
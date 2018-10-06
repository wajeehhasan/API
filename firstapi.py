from pyfiglet import figlet_format
from termcolor import colored
import requests


def jokes(topic):
	#data gathering
	url = "https://icanhazdadjoke.com/search"
	response = requests.get(url, 
		headers={"Accept":"application/json"},
		params={"term":topic}
		)
	data=response.json()
	print(data)
	#end
	#welcome banner
	asci_text=figlet_format("DAD JOKES 3000")
	clr_ascii_text=colored(asci_text, color="magenta",on_color="on_green", attrs=["blink"])
	#end
	print("\nI have {} jokes on {}".format(data["total_jokes"],data["search_term"]))



topic=input("\nlet me tell you a joke! give me a topic : ")
jokes(topic)
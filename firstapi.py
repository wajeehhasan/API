from pyfiglet import figlet_format
from termcolor import colored
from requests import get
import random



def jokes(topic):
	#data gathering
	url = "https://icanhazdadjoke.com/search"
	response = get(url, 
		headers={"Accept":"application/json"},
		params={"term":topic}
		)
	data=response.json()
	total_jokes_int=int(data["total_jokes"]) #to check for condition if there are jokes or no
	#end
	#welcome banner
	asci_text=figlet_format("DAD JOKES 3000")
	clr_ascii_text=colored(asci_text, color="magenta",on_color="on_green", attrs=["blink"])
	print(clr_ascii_text)
	#end
	if total_jokes_int==0:
		print("\nSorry i have no jokes on this topic try other Topic :( Try again :( ")
	elif total_jokes_int>0:
		#joke selection and filtering
		joke_lists=data["results"]
		len_jk=len(joke_lists)
		filtered_list=[]
		for wrd in joke_lists:
			filtered_list.append(wrd["joke"])
		#end
		#check Cases
		total_jokes_int=int(data["total_jokes"])
		#end
		#random selection of joke
		print("\nI have got {} jokes on the topic : {}".format(data["total_jokes"],data["search_term"]))
		print("\n Here's One ")
		random.shuffle(filtered_list)
		print(filtered_list.pop())
		print("\n\n")
		#end


topic=input("\nlet me tell you a joke! give me a topic : ")
jokes(topic)
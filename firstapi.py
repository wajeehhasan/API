from pyfiglet import figlet_format
from termcolor import colored
import requests


def jokes(topic):
	url = "https://icanhazdadjoke.com/search"
	response = requests.get(url, 
		headers={"Accept":"application/json"},
		params={"term":"cat"}
		)
	data=response.json()
	print(data)


jokes("cat")
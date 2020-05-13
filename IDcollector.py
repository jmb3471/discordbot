import json
import requests
import auth

URL_START = "http://www.omdbapi.com/?t="
URL_END = "&apikey=" + auth.API_KEY

def getByName(name):
	nameParts = name.split()
	url_Title = ""
	for i in range(0, len(nameParts)):
		url_Title += nameParts[i]
		if i <= len(nameParts) - 1:
			url_Title += "+"
	response = requests.get(URL_START + url_Title + URL_END)
	dict = response.json()
	print(dict)

	return dict["imdbID"]

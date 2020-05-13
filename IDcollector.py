import json
import requests
import auth

URL_START = "http://www.omdbapi.com/?t="
URL_END = "&apikey=" + auth.API_KEY

def getByName(name):
	json = get(URL_START + name + URL_END)

	dict = json.loads(json)
	print(dict["id"])

	return dict["id"]

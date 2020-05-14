import json
from requests import get
import auth

URL_START = "http://www.omdbapi.com/?t="
URL_END = "&plot=short&apikey=" + auth.API_KEY

def getID(title):
	movieFile = getJSONFile(title)
	return movieFile["imdbID"]

def getDirector(title):
	movieFile = getJSONFile(title)
	try:
		return movieFile["Director"]
	except KeyError:
		return "None"

def getIMDBRating(title):
	movieFile = getJSONFile(title)
	try:
		return movieFile["imdbRating"]
	except KeyError:
		return "N/A"

def getPlot(title):
	return getJSONFile(title)["Plot"]


def getJSONFile(title):
	title = title.replace('\'', '')
	nameParts = title.split()
	url_Title = ""
	for i in range(0, len(nameParts)):
		url_Title += nameParts[i]
		if i < len(nameParts) - 1:
			url_Title += "+"
	response = requests.get(URL_START + url_Title + URL_END)
	dict = response.json()

	return dict
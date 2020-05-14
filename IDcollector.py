import json
import requests
import auth
import random

URL_START = "http://www.omdbapi.com/?t="
URL_END = "&plot=short&apikey=" + auth.API_KEY

def getID(title):
	try:
		movieFile = getJSONFile(title)
		return movieFile["imdbID"]
	except KeyError:
		return "N/A"

def getDirector(title):
	movieFile = getJSONFile(title)
	try:
		return movieFile["Director"]
	except KeyError:
		return "None"

def getimdbVotes(title):
	return getJSONFile(title)["imdbVotes"]

def getIMDBRating(title):
	movieFile = getJSONFile(title)
	try:
		return movieFile["imdbRating"]
	except KeyError:
		return "N/A"

def getPlot(title):
	try:
		return getJSONFile(title)["Plot"]
	except KeyError:
		return "N/A"
def get_recommended(title):
	try:
		url = "https://api.themoviedb.org/3/movie/" + getID(title) + "/similar?api_key=" + auth.TMDB_API_KEY + "&language=en-US&page=1"
		response = requests.get(url)
		dict = response.json()
		return random.choice(dict["results"])["title"]
	except KeyError:
		return "Unable to find recommendation"

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
	print(dict)
	return dict
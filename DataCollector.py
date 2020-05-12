from requests import get
from bs4 import BeautifulSoup
from warnings import warn
from time import sleep
from random import randint
#import numpy as np

#pages = np.arramge(1, 9951, 50)
pages = [1, 51, 101, 151]
genres = ["sci-fi",
          "animation",
          "action",
          "comedy",
          "adventure",
          "fantasy",
          "thriller",
          "horror",
          "mystery"]
for genre in genres:
    writeFile = open(str(genre) + "Titles", "w")
    for page in pages:
        response = get("https://www.imdb.com/search/title/?genres=" + genre + "&start=" + str(page) + "&explore=title_type,genres&ref_=adv_prv")
        page_html = BeautifulSoup(response.text, 'html.parser')

        movieContainers = page_html.find_all('div', class_ = 'lister-item mode advanced')

        for container in movieContainers:
            writeFile.write(container.h3.a.text + "\n")
    writeFile.close()
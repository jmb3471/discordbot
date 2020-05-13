from requests import get
from bs4 import BeautifulSoup
from warnings import warn
from time import sleep
from random import randint

pages = [1, 51, 101, 151, 201, 251, 301, 351, 401, 451, 501, 551, 601, 651, 701, 751, 801, 851, 901, 951]
genres = ["sci-fi",
          "animation",
          "action",
          "comedy",
          "adventure",
          "fantasy",
          "thriller",
          "horror",
          "mystery",
          "drama"]
for genre in genres:
    writeFile = open(str(genre) + "Titles.txt", "w")
    for page in pages:
        response = get("https://www.imdb.com/search/title/?genres=" + genre + "&start=" + str(page) + "&explore=title_type,genres&ref_=adv_prv")
        page_html = BeautifulSoup(response.text, 'html.parser')

        movieContainers = page_html.find_all('div', class_ = 'lister-item mode-advanced')

        for container in movieContainers:
            if container.find('div', class_ = 'ratings-metascore') is not None:
                rating = int(container.find('span', class_ = 'metascore').text)
                if rating > 60:
                    writeFile.write(container.h3.a.text + "\n")
    writeFile.close()
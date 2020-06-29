from requests import get
from bs4 import BeautifulSoup
from random import randint
import threading
import numpy as np
import IDcollector
import Encryption
import auth

pages = np.arange(1001, 1951, 50)
threads = []
genre_Threads = []
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


#Each thread for each page runs this
def collect_info(type, page_num, write_file):
    response = get("https://www.imdb.com/search/title/?genres=" + type + "&start=" + str(
        page_num) + "&explore=title_type,genres&ref_=adv_prv")
    page_html = BeautifulSoup(response.text, 'html.parser')

    movie_containers = page_html.find_all('div', class_='lister-item mode-advanced')

    for container in movie_containers:
        try:
            rating = container.strong.text
            rating = rating.replace(',', '')
        except AttributeError:
            rating = "N/A"
        if rating != "N/A":
            rating = float(rating)
            try:
                votes = container.find('span', attrs = {'name' : 'nv'})['data-value']
                votes = votes.replace(',', '')
                votes = int(votes)
            except TypeError:
                votes = 0
            if rating > 7.0 and votes > 25000:
                write_file.write(container.h3.a.text + "\n")


#Creates a thread for each page and runs the above method
def get_genre_info(genre_search):
    if pages[0] == 1:
        writefile = open("GenreLists/" + str(genre_search) + "Titles.txt", "w")
    else:
        writefile = open("GenreLists/" + str(genre_search) + "Titles.txt", "a")
    for page in pages:
        threads.append(threading.Thread(target=collect_info, args=(genre_search, page, writefile)))
        threads[len(threads) - 1].start()
    for thread in threads:
        thread.join()
    writefile.close()


#Ran out of threads so we have to do 4 at a time for genres

def rundata():
    for i in range(0, len(genres)):
        genre_Threads.append(threading.Thread(target=get_genre_info, args=(genres[i],)))
        genre_Threads[len(genre_Threads) - 1].start()
    for genre_Thread in genre_Threads:
        genre_Thread.join()
    '''for i in range(5, len(genres)):
        genre_Threads.append(threading.Thread(target=get_genre_info, args=(genres[i],)))
        genre_Threads[len(genre_Threads) - 1].start()
    for genre_Thread in genre_Threads:
        genre_Thread.join()'''


rundata()
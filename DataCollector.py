from requests import get
from bs4 import BeautifulSoup
from random import randint
import threading
import numpy as np

pages = np.arange(1, 4951, 50)
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
        if container.find('div', class_='ratings-metascore') is not None:
            rating = int(container.find('span', class_='metascore').text)
            if rating > 60:
                write_file.write(container.h3.a.text + "\n")


#Creates a thread for each page and runs the above method
def get_genre_info(genre_search):
    writefile = open("GenreLists/" + str(genre_search) + "Titles.txt", "w")
    for page in pages:
        threads.append(threading.Thread(target=collect_info, args=(genre_search, page, writefile)))
        threads[len(threads) - 1].start()
    for thread in threads:
        thread.join()
    writefile.close()


#Ran out of threads so we have to do 4 at a time for genres

def rundata():
    for i in range(0, 4):
        genre_Threads.append(threading.Thread(target=get_genre_info, args=(genres[i],)))
        genre_Threads[len(genre_Threads) - 1].start()
    for genre_Thread in genre_Threads:
        genre_Thread.join()
    for i in range(4, len(genres) - 1):
        genre_Threads.append(threading.Thread(target=get_genre_info, args=(genres[i],)))
        genre_Threads[len(genre_Threads) - 1].start()
    for genre_Thread in genre_Threads:
        genre_Thread.join()
    get_genre_info(genres[len(genres) - 1])

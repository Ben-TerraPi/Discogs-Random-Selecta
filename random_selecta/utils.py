import pandas as pd
import requests
import operator
import csv
import pprint
import random
import discogs_client


token = "FFCHhXOkwaGQGbBGejcGGYsdUngQcVZjbijuCVrZ"

d = discogs_client.Client("ExampleApplication/0.1", user_token= token)

#>>>>>>>>>>>>>>>>>>>>>>>> Random SELECTA

def random_selecta(genre,style, year):
    results = d.search(genre=genre,style=style, year=year)
    test = len(results)
    if test != 0:
        page_random = random.randint(1,results.pages)
        nb_results = len(results.page(page_random))
        k_random = random.randint(0,nb_results-1)
        album = results.page(page_random)[k_random]
        title = album.title
        image = album.images[0]["uri"]
        str = title.lower()
        str2 = str.replace(" ","+")
        url = f'https://www.youtube.com/results?search_query={str2}'
        link = album.url

        #webbrowser.open(url)

        return title, image, url , link 
    else:
        return "todo"


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>start

def random_title1(genre, year):
    list = []
    results = d.search(genre=genre,year=year)
    for el in results:
        list.append(el)
    return pd.DataFrame(list)
   

def random_title2(genre, year):
    results = d.search(genre=genre,year=year)
    test = len(results)
    if test != 0:
        page_random = random.randint(1,results.pages)
        nb_results = len(results.page(page_random))
        k_random = random.randint(0,nb_results-1)
        return results.page(page_random)[k_random]
    else:
        return "todo"



#------------------------------------Random SELECTA

def random_genre_album(genre, year):
    results = d.search(genre=genre, year=year)
    test = len(results)
    if test != 0:
        page_random = random.randint(1,results.pages)
        nb_results = len(results.page(page_random))
        k_random = random.randint(0,nb_results-1)
        album = results.page(page_random)[k_random]
        title = album.title
        str = title.lower()
        str2 = str.replace(" ","+")
        return title, f'https://www.youtube.com/results?search_query={str2}' 
    else:
        return "todo"
    
# [0].title


def random_style_album(genre,style, year):
    results = d.search(genre=genre,style=style, year=year)
    test = len(results)
    if test != 0:
        page_random = random.randint(1,results.pages)
        nb_results = len(results.page(page_random))
        k_random = random.randint(0,nb_results-1)
        album = results.page(page_random)[k_random]
        title = album.title
        image = album.images[0]["uri"]
        str = title.lower()
        str2 = str.replace(" ","+")
        url = f'https://www.youtube.com/results?search_query={str2}'
        return title, image, url 
    else:
        return "todo"
    
# [0].title


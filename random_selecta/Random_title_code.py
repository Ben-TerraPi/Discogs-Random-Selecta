#%%
#Import
import pandas as pd
import requests
import discogs_client
import operator
import csv
import pprint
import random


#Discogs Client & User token
# %%
d = discogs_client.Client("ExampleApplication/0.1", user_token= "aPYjQukkBxJNCzDiALSJxttKmPMfuLmJDAVOOuKS")


# %%
def random_title1(genre, year):
    list = []
    results = d.search(genre=genre,year=year)
    for el in results:
        list.append(el)
    return pd.DataFrame(list)
   
# %%
random_title1("Hip Hop",1983)
# %%

# %%
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

# %%
random_title2("Reggae",1970)



#-------------------------------------------Random SELECTA

# %%
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


# %%
random_genre_album("Hip Hop", 1982)
# %%


# %%
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


# %%
random_style_album("Children's","Punk", 2015)
# %%



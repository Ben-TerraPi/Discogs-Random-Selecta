#%%
import pandas as pd
import requests
import discogs_client
import operator
import csv
import pprint
import random

#%%
#Discogs Client & User token

d = discogs_client.Client("ExampleApplication/0.1", user_token= "aPYjQukkBxJNCzDiALSJxttKmPMfuLmJDAVOOuKS")

#%%
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
        return title, image, f'https://www.youtube.com/results?search_query={str2}' 
    else:
        return "todo"
    

#%%
random_style_album("","Italo-Disco",1982)

# %%

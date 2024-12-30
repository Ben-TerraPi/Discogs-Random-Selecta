import pandas as pd
import requests
import operator
import csv
import pprint
import random
import discogs_client
import streamlit as st
# from googleapiclient.discovery import build

#Discogs Client & User token

token = st.secrets["token"]["user_token"]

d = discogs_client.Client("ExampleApplication/0.1", user_token= token)

#>>>>>>>>>>>>>>>>>>>>>>>> Random SELECTA

def random_selecta(genre,style, year):
    results = d.search(genre=genre,style=style, year=year)
    test = len(results)
    if test != 0:

        #album aléatoire
        page_random = random.randint(1,results.pages)
        nb_results = len(results.page(page_random))
        k_random = random.randint(0,nb_results-1)
        album = results.page(page_random)[k_random]

        #info album
        title = album.title
        image = album.images[0]["uri"]
        link = album.url

        #youtube search
        str = title.lower()
        str2 = str.replace(" ","+")
        url = f'https://www.youtube.com/results?search_query={str2}'
        
        #webbrowser.open(url)

        return title, image, url , link 
    else:
        return "todo"


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>LIST ALBUMS

def random_title1(genre, year):
    list = []
    results = d.search(genre=genre,year=year)
    for el in results:
        list.append(el)
    return pd.DataFrame(list)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>RANDOM ALBUM

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



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Random SELECTA GENRE

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

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Random SELECTA GENRE + STYLE

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

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> test youtube


def random_youtube(genre, style, year):

    results = d.search(genre=genre,style=style, year=year)
    test = len(results)
    if test != 0:

        #album aléatoire
        page_random = random.randint(1,results.pages)
        nb_results = len(results.page(page_random))
        k_random = random.randint(0,nb_results-1)
        album = results.page(page_random)[k_random]

        #info album
        title = album.title
        image = album.images[0]["uri"]
        link = album.url

        #youtube search
        str = title.lower()
        str2 = str.replace(" ","+")
        url = f'https://www.youtube.com/results?search_query={str2}'
        
        #webbrowser.open(url)

        # Recherche sur YouTube via l'API YouTube
        youtube = build('youtube', 'v3', developerKey=api_key)
        request = youtube.search().list(
            part="snippet",
            q=str2,
            type="video",
            maxResults=5  # Limiter le nombre de résultats
        )
        response = request.execute()

        # Extraire les résultats de la recherche YouTube
        youtube_results = []
        for item in response['items']:
            video_id = item['id']['videoId']
            video_title = item['snippet']['title']
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            youtube_results.append({'title': video_title, 'url': video_url})

        return title, image, url , link , youtube_results
    else:
        return "Aucun résultat trouvé"

print("utils.py loaded successfully")
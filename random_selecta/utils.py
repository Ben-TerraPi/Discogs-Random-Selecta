import pandas as pd
import random
import discogs_client
import streamlit as st
from googleapiclient.discovery import build

#Discogs Client & User token

token = st.secrets["token"]["user_token"]

d = discogs_client.Client("ExampleApplication/0.1", user_token= token)

#>>>>>>>>>>>>>>>>>>>>>>>>>>YOUTUBE


api_key = st.secrets["youtube"]["api_key"]


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>LIST ALBUMS

def list_albums(genre, year):
    list = []
    results = d.search(genre=genre,year=year)
    for el in results:
        list.append(el)
    return pd.DataFrame(list)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>RANDOM ALBUM

def random_album(genre, year):
    results = d.search(genre=genre,year=year)
    test = len(results)
    if test != 0:
        page_random = random.randint(1,results.pages)
        nb_results = len(results.page(page_random))
        k_random = random.randint(0,nb_results-1)
        return results.page(page_random)[k_random]
    else:
        return "todo"

#>>>>>>>>>>>>>>>>>>>>>>>> Random SELECTA no videos

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
        

        return title, image, url , link 
    else:
        return "todo"


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> randm selecta + youtube


def random_youtube(genre, style, year):
    results = d.search(genre=genre, style=style, year=year)
    test = len(results)

    # Valeurs par défaut
    title = None
    image = "image/default_cover.png" 
    url = None
    link = None
    discogs_videos = None
    youtube_results = []
    
    # Si des résultats sont trouvés
    if test != 0:
        # Album aléatoire
        page_random = random.randint(1, results.pages)
        nb_results = len(results.page(page_random))
        k_random = random.randint(0, nb_results - 1)
        album = results.page(page_random)[k_random]

        if album:

            # Info album
            title = album.title
            if hasattr(album, 'images') and album.images:
                image = album.images[0]["uri"]
            link = album.url

            # Recherche Youtube
            str = title.lower()
            str2 = str.replace(" ", "+")
            str3 = str2.replace("&", "and")
            url = f'https://www.youtube.com/results?search_query={str3}'

            # Vidéo Discogs
            if hasattr(album, 'videos') and album.videos:
                nb = len(album.videos)
                if nb > 0:
                    key_random = random.randint(0, nb - 1)
                    discogs_videos = album.videos[key_random].url
            else:
                # API YouTube
                youtube = build('youtube', 'v3', developerKey=api_key)
                request = youtube.search().list(
                    part="snippet",
                    q=str3,
                    type="video",
                    maxResults=1
                )
                try:
                    response = request.execute()
                except:
                    response = None

                # Résultats recherche YouTube
                if response:
                    youtube_results = []
                    for item in response['items']:
                        video_id = item['id']['videoId']
                        video_title = item['snippet']['title']
                        video_url = f"https://www.youtube.com/watch?v={video_id}"
                        youtube_results.append({'title': video_title, 'url': video_url})

    return title, image, url, link, discogs_videos, youtube_results, test


print("utils.py loaded successfully")


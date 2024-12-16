import discogs_client
import random
import webbrowser

#%%
#Discogs Client & User token

d = discogs_client.Client("ExampleApplication/0.1", user_token= "aPYjQukkBxJNCzDiALSJxttKmPMfuLmJDAVOOuKS")

#-------------------------GENRES DISCOGS
#%%
list_genre = [
"Blues", 
"Brass & Military ",
"Children's",
"Classical", 
"Electronic",
"Folk, World, & Country", 
"Funk / Soul",
"Hip Hop", 
"Jazz", 
"Latin",
"Non-Music",
"Pop",
"Reggae",
"Rock", 
"Stage & Screen"
]

#%%
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

        webbrowser.open(url)

        return title, image, url  
    else:
        return "todo"
    

#%%
random_selecta("Rock","",1987)


# %%

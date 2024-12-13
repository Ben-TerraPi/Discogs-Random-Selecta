# %%
#Import
import pandas as pd
import requests
import discogs_client
import operator
import csv
import pprint


#Discogs Client & User token
# %%
d = discogs_client.Client("ExampleApplication/0.1", user_token= "aPYjQukkBxJNCzDiALSJxttKmPMfuLmJDAVOOuKS")


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>test samidou>>>> Aphex twin

print(dir(d.artist(45)))


phex = d.artist(45)

r = phex.releases
len(r)

for element in r :
  print(element)



# %%
#forum API
artists = d.search("Laurent Garnier", type='artist')
first_found_artist = artists.page(0)[0].data
release_dic = d.artist(first_found_artist['id']).releases
first_found_release = release_dic.page(0)[0].data
print(artists)
print(first_found_artist)
print(release_dic)
print(first_found_release)

# First we try the 'lesser' unique id, then the better (but not always existing) main_release...
if "id" in first_found_release:
    search_id = first_found_release['id']
    
if "main_release" in first_found_release:
    search_id = first_found_release['main_release']
              
try:
    release_details = d.release(search_id)
    genres_dic = release_details.genres
        
except Exception:
    # if no genre is found, we use the "allmighty" (but meaningless) Pop ;-)
    print ("! EXCEPTION while using search_id...")
    first_found_genre = "Pop"

try:
    styles_dic = release_details.genres
    print ("! DEBUG - Found", len(styles_dic), "styles:", styles_dic)
        
except Exception:
    pass



# %%
list = []
results = d.search(genre="Hip Hop",year=1982)
len(results)
for el in results:
    list.append(el)


l = pd.DataFrame(list)
l



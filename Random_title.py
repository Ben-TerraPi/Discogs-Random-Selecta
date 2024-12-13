# %%
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


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>test samidou>>>> Aphex twin

print(dir(d.artist(45)))


phex = d.artist(45)

r = phex.releases
len(r)

for element in r :
  print(element)


# %%
list = []
results = d.search(genre="Hip Hop",year=1982)
len(results)
for el in results:
    list.append(el)


l = pd.DataFrame(list)
l

#


# input1 = input("Genre: ")
# input2 = input("Year: ")
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
random_title2("Electronic",2005)

# %%

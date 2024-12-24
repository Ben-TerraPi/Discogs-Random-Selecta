# %%
import pandas as pd
import requests
import operator
import csv
import pprint
import random
import discogs_client


token = "FFCHhXOkwaGQGbBGejcGGYsdUngQcVZjbijuCVrZ"

d = discogs_client.Client("ExampleApplication/0.1", user_token= token)

#>>>>>>>>>>>>>>>>>>>>>>>> FUNCTION

def random_title1(genre, year):
    list = []
    results = d.search(genre=genre,year=year)
    for el in results:
        list.append(el)
    return pd.DataFrame(list)
   
# %%
random_title1("Hip Hop",1983) 

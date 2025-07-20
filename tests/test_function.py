# %%
import pandas as pd
import random
import discogs_client
import streamlit as st


token = st.secrets["token"]["user_token"]

d = discogs_client.Client("ExampleApplication/0.1", user_token= token)

#>>>>>>>>>>>>>>>>>>>>>>>> FUNCTIONS

# def list_albums(genre, year):
#     list = []
#     results = d.search(genre=genre,year=year)
#     for el in results:
#         list.append(el)
#     return pd.DataFrame(list)
   
# # %%
# list_albums("Hip Hop",1986) 

#%%
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

#%%
print(dir(random_album("hip hop", 1986)))


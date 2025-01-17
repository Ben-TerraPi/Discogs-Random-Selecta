# %%
import pandas as pd
import discogs_client
import streamlit as st


token = st.secrets["token"]["user_token"]

d = discogs_client.Client("ExampleApplication/0.1", user_token= token)

#>>>>>>>>>>>>>>>>>>>>>>>> FUNCTION

def list_albums(genre, year):
    list = []
    results = d.search(genre=genre,year=year)
    for el in results:
        list.append(el)
    return pd.DataFrame(list)
   
# %%
list_albums("Hip Hop",1983) 

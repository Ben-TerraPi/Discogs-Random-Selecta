import pandas as pd
import discogs_client
import streamlit as st
from utils import export_tracks_to_csv , create_my_tracks_csv

# Discogs Client & User token

token = st.secrets["token"]["user_token"]
d = discogs_client.Client("ExampleApplication/0.1", user_token= token)

me = d.identity()

export_tracks_to_csv(me)

df = pd.read_csv("collection_tracks.csv")

create_my_tracks_csv(df)
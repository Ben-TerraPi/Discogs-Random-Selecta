import discogs_client
import streamlit as st
from utils import export_collection_to_csv

# Discogs Client & User token

token = st.secrets["token"]["user_token"]
d = discogs_client.Client("ExampleApplication/0.1", user_token=token)

# Mon compte

me = d.identity()
print(dir(me))

print(me.id)
print(me.location)
print(me.name)
print(me.url)

# # list collection
# data = []
# for item in me.collection_folders[0].releases:
#     data.append(item)

# Création du CSV
export_collection_to_csv(me)
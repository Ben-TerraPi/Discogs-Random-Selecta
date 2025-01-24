#Import
import pandas as pd
import pandas_gbq
import requests
import discogs_client
import operator
import csv
import pprint
import streamlit as st


#Discogs Client & User token

token = st.secrets["token"]["user_token"]
d = discogs_client.Client("ExampleApplication/0.1", user_token= token)


#Mon compte

me = d.identity()
print(dir(me))

print(me.id)
print(me.location)
print(me.name)
print(me.url)


#list collection
data = []
for item in me.collection_folders[0].releases:
      data.append(item)


#Import de ma Collection

# Export fichier CSV
with open('collection.csv',
          'w',
          newline='',
          encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        'id',
        'title',
        'artist',
        'year',
        'genre',
        'style',
        'master_id',
        'release_country',
        'labels',
        'format',
        'rating',
        'have',
        'want',
        'url',
        'image_url'
    ])

    for release in data:
        release_data = release.release

        genres = ", ".join(release_data.genres) if release_data.genres else "N/A"
        styles = ", ".join(release_data.styles) if release_data.styles else "N/A"
        master_id = release_data.master.id if release_data.master else "N/A"
        country = release_data.country if release_data.country else "N/A"
        labels = ", ".join([label.name for label in release_data.labels]) if release_data.labels else "N/A"
        formats = ", ".join([", ".join(fmt['descriptions']) for fmt in release_data.formats]) if release_data.formats else "N/A"
        community_rating = (
             release_data.community.rating.average if release_data.community and release_data.community.rating else "N/A"
        )
        community_have = release_data.community.have if release_data.community.have else "N/A"
        community_want = release_data.community.want if release_data.community.want else "N/A"
        image_url = release_data.images[0]["uri"] if release_data.images else "N/A"

        writer.writerow([
            release.id,
            release_data.title,
            release_data.artists[0].name if release_data.artists else "N/A",
            release_data.year,
            genres,
            styles,
            master_id,
            country,
            labels,
            formats,
            community_rating,
            community_have,
            community_want,
            release_data.url,
            image_url
        ])

print("Collection exportée dans 'collection.csv'.")

#Export de ma collection trié

my_collection = pd.read_csv("collection.csv")

# tri du tableau par nom artiste
my_collection = my_collection.sort_values("artist")

# reset de l'index du tableau
my_collection = my_collection.reset_index()

#suppression de l'ancienne colonne index
my_collection = my_collection.drop("index",axis=1)

#export du nouveau tableau .csv
my_collection.to_csv("my_collection.csv")


#>>>>>>>>>>>>>>>>>> Export vers Bigquery

project_id = "discogs-random-selecta"
table_id = "discogs-random-selecta.my_data.my_collection"

pandas_gbq.to_gbq(my_collection, table_id, project_id)

print("tableau exporté")








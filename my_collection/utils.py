import discogs_client
import streamlit as st
import csv
import pandas as pd
import re

# Discogs Client & User token

token = st.secrets["token"]["user_token"]
d = discogs_client.Client("ExampleApplication/0.1", user_token= token)

# Mon compte

me = d.identity()

#############################################################################################################

def export_collection_to_csv(me):
    ''' export de ma collection personnelle depuis Discogs'''
    # list collection
    data = []
    for item in me.collection_folders[0].releases:
        data.append(item)

    # Import de ma Collection

    # Création du CSV
    with open('collection.csv', 'w', newline='', encoding='utf-8') as csvfile:
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

            artist_name = release_data.artists[0].name
            artist_name = re.sub(r'\(\d+\)', '', artist_name).strip()
            genres = ", ".join(release_data.genres) if release_data.genres else "N/A"
            styles = ", ".join(release_data.styles) if release_data.styles else "N/A"
            master_id = release_data.master.id if release_data.master else "N/A"
            labels = ", ".join([label.name for label in release_data.labels]) if release_data.labels else "N/A"
            formats = ", ".join([", ".join(fmt['descriptions']) for fmt in release_data.formats]) if release_data.formats else "N/A"
            image_url = release_data.images[0]["uri"] if release_data.images else "N/A"

            writer.writerow([
                release.id,
                release_data.title,
                artist_name,
                release_data.year,
                genres,
                styles,
                master_id,
                release_data.country,
                labels,
                formats,
                release_data.community.rating.average,
                release_data.community.have,
                release_data.community.want,
                release_data.url,
                image_url
            ])

    print("Collection importée dans 'collection.csv'.")

#########################################################################################################

def export_tracks_to_dataframe(me):
    ''' expot de mes track dans un dataframe avant nettoyage et création du csv'''
    # List collection
    data = []
    for item in me.collection_folders[0].releases:
        data.append(item)

    # track data
    tracklist_data = []

    for item in data:
        item_data = item.release

        artist_name = item_data.artists[0].name
        artist_name = re.sub(r'\(\d+\)', '', artist_name).strip()

        # Extract track information
        tracklist_str = str(item_data.tracklist)
        pattern = r"<Track '([^']+)' '([^']+)'>"
        matches = re.findall(pattern, tracklist_str)

        for track_id, track_name in matches:
            tracklist_data.append({
                "album_id": item.id,
                "artist": artist_name,
                "album": item_data.title,
                "track_id": f"{item.id}_{track_id}",
                "title": track_name
            })

    # Create DataFrame
    df_tracklist = pd.DataFrame(tracklist_data)

    return df_tracklist

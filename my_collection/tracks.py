import pandas as pd
import discogs_client
import csv
import re
import streamlit as st
from utils import export_tracks_to_dataframe

# Discogs Client & User token

token = st.secrets["token"]["user_token"]
d = discogs_client.Client("ExampleApplication/0.1", user_token= token)

me = d.identity()

# def export_tracks_to_csv(me):
#     # list collection
#     data = []
#     for item in me.collection_folders[0].releases:
#         data.append(item)

#     # Création du 1er CSV
#     with open('collection_tracks.csv', 'w', newline='', encoding='utf-8') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(['id', 'artist', 'album', 'tracklist'])

#         for item in data:
#             item_data = item.release

#             artist_name = item_data.artists[0].name
#             artist_name = re.sub(r'\(\d+\)', '', artist_name).strip()

#             writer.writerow([
#                 item.id,
#                 artist_name,
#                 item_data.title,
#                 item_data.tracklist
#             ])

#     print("1er csv créé")

# df = pd.read_csv("collection_tracks.csv")

# #fonction pour extraire le nom des tracks pour création de lignes unique
# def extract_tracks(row):
#     tracklist_str = row["tracklist"]
#     pattern = r"<Track '([^']+)' '([^']+)'>"  
#     matches = re.findall(pattern, tracklist_str)
#     new_rows = []
#     for track_id, track_name in matches:
#         new_rows.append({
#             "album_id": row["id"],
#             "artist": row["artist"],
#             "album": row["album"],
#             "track_id": f"{row['id']}_{track_id}",
#             "title": track_name
#         })
    
#     return new_rows

# #transformation et reconstruction DataFrame
# tracklist_data = []
# for _, row in df.iterrows():
#     try:
#         tracklist_data.extend(extract_tracks(row))
#     except Exception as e:
#         print(f"Erreur {_}: {e}")
        
# df_tracklist = pd.DataFrame(tracklist_data)

# # Création du 2eme CSV
# df_tracklist.to_csv("my_tracks.csv", index=False)

# print("2eme csv créé")


# Call the function to get the DataFrame
df_tracklist = export_tracks_to_dataframe(me)

# Save the DataFrame to CSV
df_tracklist.to_csv("my_tracks.csv", index=False)

print("CSV créé")
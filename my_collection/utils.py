import discogs_client
import streamlit as st
import re

# Discogs Client & User token

token = st.secrets["token"]["user_token"]
d = discogs_client.Client("ExampleApplication/0.1", user_token= token)

# Mon compte

me = d.identity()

def export_collection_to_csv(me):
    try:
        # List collection
        data = []
        for item in me.collection_folders[0].releases:
            data.append(item)

        # data 
        releases_data = []
        for release in data:
            try:
                release_data = release.release

                artist_name = release_data.artists[0].name
                artist_name = re.sub(r'\(\d+\)', '', artist_name).strip()
                genres = ", ".join(release_data.genres) if release_data.genres else "N/A"
                styles = ", ".join(release_data.styles) if release_data.styles else "N/A"
                master_id = release_data.master.id if release_data.master else "N/A"
                labels = ", ".join([label.name for label in release_data.labels]) if release_data.labels else "N/A"
                formats = ", ".join([", ".join(fmt['descriptions']) for fmt in release_data.formats]) if release_data.formats else "N/A"
                image_url = release_data.images[0]["uri"] if release_data.images else "N/A"

                releases_data.append([
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
            except Exception as e:
                print(f"Error {release.id}: {e}")
                continue

        # DataFrame and CSV
        df = pd.DataFrame(releases_data, columns=[
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

        df.to_csv('collection.csv', index=False, encoding='utf-8')
        print("Collection exportée dans 'collection.csv'.")

    except Exception as e:
        print(f"An error occurred: {e}")
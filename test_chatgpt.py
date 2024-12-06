#Import
import pandas as pd
import requests
import discogs_client
import operator
import csv
import pprint


#Discogs Client & User token

d = discogs_client.Client("ExampleApplication/0.1", user_token= "aPYjQukkBxJNCzDiALSJxttKmPMfuLmJDAVOOuKS")



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>         RELEASE APHEX TWIN
phex = d.artist(45)

for release in phex.releases:
    # Afficher les informations de chaque sortie
    print(f"Title: {release.title}")
    print(f"Year: {release.year}")
    #print(f"Type: {release.type}")
    print(f"URL: {release.url}")
    print('-' * 30)

# z = []
# for release in phex.releases:
#     # Vérifier si l'objet est de type Release ou Master
#     if isinstance(release, discogs_client.models.Master):
#         # Si c'est un Master, on peut accéder à ses releases
#     z.append(release.title)

# len(z)

for release in phex.releases:
    if isinstance(release, discogs_client.Master):
        # Vérifiez les formats et descriptions
        formats = release.data.get("formats", [])
        descriptions = [desc for f in formats for desc in f.get("descriptions", [])]

        # Filtre : inclure uniquement les albums
        if "Album" in descriptions and not any(desc in ["Compilation", "Single", "EP"] for desc in descriptions):
            albums.append({
                'title': release.title,
                'year': release.year,
                'id': release.id
            })

# Tri des albums par année de sortie
albums_sorted = sorted(albums, key=lambda x: x['year'])

# Affichage des résultats
for album in albums_sorted:
    print(f"{album['year']} - {album['title']} (ID: {album['id']})")
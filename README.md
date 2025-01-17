En construction!!!



# About it :  ![image](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Discogs-logo-billboard-1548-1092x722.jpg/320px-Discogs-logo-billboard-1548-1092x722.jpg)
Discogs is a database of information about audio recordings, including commercial releases, promotional releases, and bootleg or off-label releases.

Database contents are user-generated, and described in The New York Times as "Wikipedia-like".

While the site was originally created with the goal of becoming the largest online database of electronic music, it now includes releases in all genres and on all formats.

SITE: https://www.discogs.com/

API: https://api.discogs.com/

DOC:

https://python3-discogs-client.readthedocs.io/en/latest/index.html

https://www.discogs.com/developers/

# About me:

Je suis passionné de musique et collectionneur de vinyl, discogs est un site où je passe beaucoup de temps. Suite à une formation de Data Analyst, il était évident que pour mon premier projet personnel j'allais combiner ces deux centres d'intérêt.

Au départ ma volonté était de simplement lister ma collection personnel en utilisant python et l'API de discogs, il s'est vite avéré que je n'avais pas l'envie de m'arréter là.


# 1er dossier : [my_collection](https://github.com/Ben-TerraPi/Discogs/tree/main/my_collection) 

## scrap_discogs.py

J'ai commencé en utilisant google collab étant gratuit et simple d'utilisation avec cette première ligne de code:

`! pip install python3-discogs-client`

C'était partie pour le début d'un projet qui m'a passionné.

### import

```
import discogs_client
import csv
import pandas as pd 
```

### Discogs Client & User token

Je me suis connecté à mon compte grâce à la génération d'un token développeur personnel qui m'a permis de naviguer dans l'API discogs.

```
d = discogs_client.Client("ExampleApplication/0.1", user_token= "secret")
me = d.identity()
```

### Mon compte

```
print(dir(me))
```

J'avais maintenant les attributs disponible pour mon compte client:

['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_known_invalid_keys', 'changes', 'client', 'collection_folders', 'collection_items', 'collection_value', 'data', 'delete', 'fetch', 'home_page', 'id', 'inventory', 'lists', 'location', 'name', 'num_collection', 'num_lists', 'num_wantlist', 'orders', 'previous_request', 'profile', 'rank', 'rating_avg', 'refresh', 'registered', 'releases_contributed', 'save', 'url', 'username', 'wantlist']

```
print(me.id)
print(me.location)
print(me.name)
print(me.url)
print(me.collection_folders)
```
A savoir:

* 2794711
* Rennes
* TerraPi
* https://www.discogs.com/user/Little.Red.Roquet
* [<CollectionFolder 0 'All'>, <CollectionFolder 1 'Uncategorized'>, ...

Avoir la liste de tous mes vinyles était aussi simple que cela

```
data = []
for item in me.collection_folders[0].releases:
      data.append(item)
```
### Import de ma Collection

Il était temps de créer le tableau .csv regroupant ma collection avec les informations de mon choix:

| id  | title | artist | year | genre | style | master_id | release_country | labels | format | rating | have | want | url | image_url |
|-----|-------|--------|------|-------|-------|-----------|-----------------|--------|--------|--------|------|------|-----|-----------|

```
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
```
### Création du fichier final

Le scraping via l'API n'a pas nécissité un nettoyage conséquant. 

```
# load fichier .csv
df = pd.read_csv("/content/collection.csv")

# tri du tableau par nom artiste
df = df.sort_values("artist")

# rest de l'index du tableau
df = df.reset_index()

#suppression de l'ancienne colonne index
df = df.drop("index",axis=1)

#export du nouveau tableau .csv
df.to_csv("my_collection.csv")
```
Mon tableau était créé : [my_collection.csv](https://github.com/Ben-TerraPi/Discogs/blob/main/my_collection.csv)


## Stats_coll.py

A ce stade je suis devenu plus à l'aise avec VS code studio et ayant découvert le commentaire #%% permettant des Jupyter-like code cell j'arrète de travailler avec google collab et fais des tests dans cette nouvelle fenêtre interactive sur VS code avec le fichier [Stats_coll.py](https://github.com/Ben-TerraPi/Discogs/blob/main/my_collection/Stats_coll.py) 


# 2iem dossier : [tests](https://github.com/Ben-TerraPi/Discogs/tree/main/tests)

S'ensuit une phase laborieuse de tests divers avec l'API, le contenu du site de discogs étant updater par sa communauté, son code est une accumulation de MAJ et à en croire les forums, écrits par une multitude de codeur se succédant.



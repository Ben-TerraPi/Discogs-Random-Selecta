En construction!!!



## About it :  ![image](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Discogs-logo-billboard-1548-1092x722.jpg/320px-Discogs-logo-billboard-1548-1092x722.jpg)
Discogs is a database of information about audio recordings, including commercial releases, promotional releases, and bootleg or off-label releases.

Database contents are user-generated, and described in The New York Times as "Wikipedia-like".

While the site was originally created with the goal of becoming the largest online database of electronic music, it now includes releases in all genres and on all formats.

SITE: https://www.discogs.com/

API: https://api.discogs.com/

DOC:

https://python3-discogs-client.readthedocs.io/en/latest/index.html

https://www.discogs.com/developers/

## About me:

Je suis passionné de musique et collectionneur de vinyl, discogs est un site où je passe beaucoup de temps. Suite à une formation de Data Analyst, il était évident que pour mon premier projet personnel j'allais combiner ces deux centres d'intérêt.

Au départ ma volonté était de simplement lister ma collection personnel en utilisant python et l'API de discogs, il s'est vite avéré que je n'avais pas l'envie de m'arréter là.


## [my_collection](https://github.com/Ben-TerraPi/Discogs/tree/main/my_collection) 

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

J'avais maintenant les attributs:

['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_known_invalid_keys', 'changes', 'client', 'collection_folders', 'collection_items', 'collection_value', 'data', 'delete', 'fetch', 'home_page', 'id', 'inventory', 'lists', 'location', 'name', 'num_collection', 'num_lists', 'num_wantlist', 'orders', 'previous_request', 'profile', 'rank', 'rating_avg', 'refresh', 'registered', 'releases_contributed', 'save', 'url', 'username', 'wantlist']

```
print(me.id)
print(me.location)
print(me.name)
print(me.url)
```
A savoir:

* 2794711
* Rennes
* TerraPi
* https://www.discogs.com/user/Little.Red.Roquet

Avoir la liste de tous mes vinyles était aussi simple que cela

```
data = []
for item in me.collection_folders[0].releases:
      data.append(item)
```







Query one track from a random album on Discogs by selecting a genre, a style and a year


+ code for retrieving infos from personnal collection infos 

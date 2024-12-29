#Import
import pandas as pd
import requests
import discogs_client
import operator
import csv
import pprint


#Discogs Client & User token

token = st.secrets["token"]["user_token"]

d = discogs_client.Client("ExampleApplication/0.1", user_token= token)

#Recherche sur discogs
#example MC Solaar – Prose Combat
# id = 20348713

# https://www.discogs.com/release/20348713-MC-Solaar-Prose-Combat

print(dir(d.release(20348713)))

release = d.release(20348713)

print(release.id)
print(release.title)
print(release.artists)
print(release.fetch('community'))
print(release.formats)
print(release.genres)
print(release.master)

community_details = release.community

print(community_details)
print(community_details.rating) # /5
print(community_details.want)
print(community_details.have)

print(d.release(20348713).images[0]["uri"])


#example Searching API

results = d.search('Can I borrow a feeling?')
#results = d.search('Can I borrow a feeling?', type='release')
#results = d.search('Can I borrow a feeling?', type='release,master')
#results = d.search('Can I borrow a feeling?', artist='Kirk', type='release')
#results = d.search('Can I borrow a feeling?', genre='Hip Hop')
print(results)

results = d.search('Stockholm By Night', type='release')
results.pages
artist = results[0].artists[0]
artist.name
artist.id
artist == d.artist(1)


releases = d.search('Bit Shifter', type='artist')[0].releases[1].versions[0].labels[0].releases
len(releases)
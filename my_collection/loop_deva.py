#Import
import pandas as pd
import requests
import discogs_client
import operator
import csv
import pprint


#Discogs Client & User token

d = discogs_client.Client("ExampleApplication/0.1", user_token= "aPYjQukkBxJNCzDiALSJxttKmPMfuLmJDAVOOuKS")



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>LOOP

artist_attributs = ['aliases',
                    'changes',
                    'client',
                    'data',
                    'data_quality',
                    'delete',
                    'fetch',
                    'groups',
                    'id',
                    'images',
                    'join',
                    'members',
                    'name',
                    'name_variations',
                    'previous_request',
                    'profile',
                    'real_name',
                    'refresh',
                    'releases',
                    'role',
                    'save',
                    'url',
                    'urls'
                    ]

release_attributs = ['artists',
                    'changes',
                    'client',
                    'companies',
                    'country',
                    'credits',
                    'data',
                    'data_quality',
                    'delete',
                    'fetch',
                    'formats',
                    'genres',
                    'id',
                    'images',
                    'labels',
                    'marketplace_stats',
                    'master',
                    'notes',
                    'refresh',
                    'save',
                    'status',
                    'styles',
                    'thumb',
                    'title',
                    'tracklist',
                    'url',
                    'videos',
                    'year'
                    ]

#loop artist
results_artist = []
for i in range(1,2):
  print(d.artist(i))
  print(d.artist(i).releases)
  artist_dict = {}
  for attribute in artist_attributs:
    #print(d.artist(i).attribute)
    artist_dict[attribute] = operator.attrgetter(attribute)(d.artist(i))
  results_artist.append(artist_dict)

#loop release
results_release = []
for i in range(1,2):
  print(d.release(i))
  print(d.release(i).artists)
  artist_dict = {}
  for attribute in release_attributs:
    #print(d.release(i).attribute)
    artist_dict[attribute] = operator.attrgetter(attribute)(d.release(i))
  results_release.append(artist_dict)


#Import
import pandas as pd
import requests
import discogs_client
import operator
import csv
import pprint


#Discogs Client & User token

d = discogs_client.Client("ExampleApplication/0.1", user_token= "aPYjQukkBxJNCzDiALSJxttKmPMfuLmJDAVOOuKS")


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>test samidou>>>> Aphex twin
print(dir(d.artist(45)))

phex = d.artist(45)

r = phex.releases
len(r)

for element in r :
  print(element)

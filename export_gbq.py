import pandas as pd
import pandas_gbq

collection = pd.read_csv("collection.csv")
collection_tracks = pd.read_csv("collection_tracks.csv")
my_tracks = pd.read_csv("my_tracks.csv")
tableau_genre = pd.read_csv("tableau_genre.csv")

project_id = "discogs-random-selecta"
dataset = "my_data"

dfs = [collection,
       collection_tracks,
       my_tracks,
       tableau_genre
       ]

def get_var_name(var):
    for name, value in globals().items():
        if value is var:
            return name

for df in dfs:
  table_id = f"{project_id}.{dataset}.{get_var_name(df)}"
  pandas_gbq.to_gbq(df, table_id, project_id)
  
print("tableaux exportés")
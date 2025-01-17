# %%
import pandas as pd
import plotly.express as px

#%%
coll = pd.read_csv("my_collection.csv")
print(coll.columns)

#%%
#Top 10 genre
g = coll.groupby("genre")["id"].count().sort_values(ascending=False).head(10)
print(g)

#%%
#Top 10 style
s = coll.groupby("style")["id"].count().sort_values(ascending=False).head(10)
print(s)

#%%
#Top 10 artiste
a = coll.groupby("artist")["id"].count().sort_values(ascending=False).head(10)
print(a)

#%%
#Focus electro

electro = coll[coll["genre"] == "Electronic"]
print(electro.info())

#%%
s_e = electro.groupby("style")["id"].count().sort_values(ascending=False)
print(s_e)

# %%
electro

# %%
coll["genre"].nunique()
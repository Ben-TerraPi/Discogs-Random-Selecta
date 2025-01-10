import sys
import os
sys.path.append('/mount/src/discogs/random_selecta')
import random
import webbrowser
import streamlit as st
import discogs_client
from datetime import datetime
from list_styles import electro_style, rock_style, pop_list, funk_soul_style, jazz_style, world_style,classical_style, hip_hop_style, stage_style, latin_style, reggae_style, blues_style, non_music_style, children_style, military_style, genres_styles
from utils import random_youtube
from googleapiclient.discovery import build

#Discogs Client & User token

token = st.secrets["token"]["user_token"]

d = discogs_client.Client("ExampleApplication/0.1", user_token= token)
    

#>>>>>>>>>>>>>>>>>>>>> Streamlit page

st.set_page_config(
    page_title="Discogs Random Selecta",
    page_icon="🎧",
    layout="wide",
    initial_sidebar_state="expanded",
)

#>>>>>>>>>>>>>>>>>>>>>> Streamlit sidebar

with st.sidebar:
    st.image("image/discogs.png")
    st.write("About:")
    st.caption("Query a random album on Discogs database by selecting a genre, a style and a release year.")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Title

st.title('🎧Discogs Random Selecta')

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

genre = st.selectbox("Select genre",
                     list(genres_styles.keys()),
                     index=0
                     )

styles = genres_styles[genre]

style = st.selectbox("Select style",
                     styles,
                     index=None
                     )

current_year = datetime.now().year
years = list(range(1910, current_year + 1))

year = st.selectbox("Select release year",
                    years,
                    index=None,
                    )

if st.button("Generate Link"):
    title, image, url , link , youtube_results = random_youtube(genre, style, year)
    
    if title and image and url:
        st.write(f"### Album Title: {title}")
        st.write(link)
        st.image(image, caption="Track Cover", width=150) #use_container_width=True)
        st.markdown(f"[YouTube Search Results]({url})")
        st.write(f"youtube url: {youtube_results[0]['url']}")
        st.video(youtube_results[0]["url"])
    else:
        st.warning("No results found. Try a different selection.")



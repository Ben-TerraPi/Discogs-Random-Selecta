import sys
import os
import random
import webbrowser
import streamlit as st
import discogs_client
from datetime import datetime
from list_styles import electro_style, rock_style, pop_list, funk_soul_style, jazz_style, world_style,classical_style, hip_hop_style, stage_style, latin_style, reggae_style, blues_style, non_music_style, children_style, military_style, genres_styles
from utils import token, random_selecta



#Discogs Client & User token

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
    title, image, url, link = random_selecta(genre, style, year)
    
    if title and image and url:
        st.markdown(f"[YouTube Search Results]({url})")
        st.write(f"### Track Title: {title}")
        st.write(link)
        st.image(image, caption="Track Cover", use_container_width=True)
    else:
        st.warning("No results found. Try a different selection.")



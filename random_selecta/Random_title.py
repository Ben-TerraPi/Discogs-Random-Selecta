import sys
import os
sys.path.append('/mount/src/discogs/random_selecta')
import random
import streamlit as st
from datetime import datetime
from list_styles import electro_style, rock_style, pop_list, funk_soul_style, jazz_style, world_style,classical_style, hip_hop_style, stage_style, latin_style, reggae_style, blues_style, non_music_style, children_style, military_style, genres_styles
from utils import random_youtube
from googleapiclient.discovery import build


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

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Title

st.title('🎧Discogs Random Selecta')

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Search

genre = st.selectbox("Select genre",
                     list(genres_styles.keys()),
                     index=None
                     )

styles = genres_styles.get(genre, None)

style = st.selectbox("Select style",
                     styles,
                     index=None
                     )

current_year = datetime.now().year
years = list(range(current_year, 1910, -1))

year = st.selectbox("Select release year",
                    years,
                    index=None,
                    )

if st.button("Generate Link"):
    title, image, url, link, discogs_videos, youtube_results = random_youtube(genre, style, year)

    if title:
        col1, col2 = st.columns([0.3, 0.7])

        with col1:
            if image:
                st.image(image, use_container_width=True)
            else:
                st.image("image/vinyl_discogs.jpg")

        with col2:
            st.write(f"### {title}")
            st.write(f"Discogs Release Page: {link}")
            st.write(f"YouTube Search Results: {url}")
            if youtube_results:
                st.write(f"YouTube URL: {youtube_results[0]['url']}")

        # Gestion des vidéos
        if discogs_videos:
            st.video(discogs_videos)
        elif youtube_results and len(youtube_results) > 0:
            st.video(youtube_results[0]['url'])
        else:
            st.warning(f"No video found for this release. Try [YouTube Search Results]({url})")
    else:
        st.warning("No results found. Try a different selection.")




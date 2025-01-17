import streamlit as st
from datetime import datetime
from list_styles import genres_styles
from utils import random_youtube


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



if st.button("Generate Release"):
        if genre is None or style is None or year is None:
             st.warning("Please select a genre, style, and release year before generating.")
        else:
            title, image, url, link, discogs_videos, youtube_results = random_youtube(genre, style, year)

            if title:
                col1, col2 = st.columns([0.3, 0.7])

                with col1:
                    if image:
                        st.image(image, use_container_width=True)
                    else:
                        st.image("image/vinyl_discogs.jpg")

                with col2:
                    st.write(f"## {title}")
                    st.write(f"Discogs Release Page: {link}")
                    st.write(f"YouTube Search Results: {url}")
                    if youtube_results:
                        st.write(f"### > Most Relevant Youtube Video:")

                # Gestion des vidéos
                if discogs_videos:
                    st.video(discogs_videos)
                elif youtube_results and len(youtube_results) > 0:
                    st.video(youtube_results[0]['url'])
                else:
                    st.warning(f"No video found for this release. Try [YouTube Search Results]({url})")
            else:
                st.warning("No results found. Try a different selection.")




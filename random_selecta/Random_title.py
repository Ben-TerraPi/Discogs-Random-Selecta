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
    st.image("image/logo.jpg")
    st.caption("")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Title

st.write(f'#### Digging for tracks on Discogs database!')

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Search

col1, col2 = st.columns([7,3])

with col1:

    genre = st.selectbox("Select genre  ( Sort by number of releases )",
                        list(genres_styles.keys()),
                        index=None
                        )

    styles = genres_styles.get(genre, None)

    style = st.selectbox("Select style  ( The deeper you go, the fewer results you'll find )",
                        styles,
                        index=None
                        )

    current_year = datetime.now().year
    years = list(range(current_year, 1900, -1))

    year = st.selectbox("Select release year",
                        years,
                        index=None,
                        )

with col2:
    ("")


st.write("")

if st.button("Generate Track", type="primary"):
    if genre is None or style is None or year is None:
        st.warning("Please select a genre, style, and release year before generating.")
    else:
        # Appel de la fonction random_youtube
        result = random_youtube(genre, style, year)
        
        if result is None or len(result) != 7:
            st.warning("An error occurred, no valid result returned.")
        else:
            title, image, url, link, discogs_videos, youtube_results, test = result

            if test == 0:
                st.warning("No result, choose a different year")
            elif title:
                st.write("")
                col1, col2 = st.columns([0.3, 0.7], gap="large")
                with col1:
                    st.write(f"Album found from {test} results:")
                with col2:
                    st.write("Random Track:")

                col1, col2 = st.columns([0.3, 0.7], gap="large")
                st.write("")
                with col1:
                    st.write(f"#### {title}")
                    if image:
                        st.image(image, use_container_width=True)
                    else:
                        st.image("image/vinyl_discogs.jpg")
                    st.write(f"[Discogs Release Page]({link})")
                    st.write(f"[YouTube Search Results]({url})")
                    if youtube_results:
                        st.warning("Most Relevant Youtube Video >>>")
                with col2:
                    # Gestion des vidéos
                    if discogs_videos:
                        st.video(discogs_videos)
                    elif youtube_results and len(youtube_results) > 0:
                        st.video(youtube_results[0]['url'])
                    else:
                        st.warning(f"No video found for this release. Try [YouTube Search Results]({url})")

            else:
                st.warning("No results found. Try a different selection.")

                
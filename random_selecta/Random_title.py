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
    st.divider()
    st.caption("About:")
    st.write("Discogs Random Selecta is an application developped to query the Discogs database.")
    st.write("")
    st.write("It renders a random album infos from your selections and displays an embedded music video. If no video is available, it will search directly on YouTube to find the most relevant result.")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Title

st.write(f'#### Digging for tracks on Discogs database!')

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Search

col1, col2, col3 = st.columns([3,3,3])

with col1:

    genre = st.selectbox("Select genre  ( Sort by number of releases )",
                        list(genres_styles.keys()),
                        index=None
                        )

with col2:

    styles = genres_styles.get(genre, None)

    style = st.selectbox("Select style  ( Optional )",
                        styles,
                        index=None
                        )

with col3:

    current_year = datetime.now().year
    years = list(range(current_year, 1950, -1))

    year = st.selectbox("Select release year ( Optional )",
                        years,
                        index=None,
                        )

st.write("")

if st.button("Generate Track", type="primary", use_container_width=True):
    if genre is None:
        st.warning("Please select a genre before generating.")
    else:   # Appel de la fonction random_youtube
        if style is None and year is None:
            result = random_youtube(genre=genre)
        elif style is None:
            result = random_youtube(genre=genre, year=year)
        elif year is None:
            result = random_youtube(genre=genre, style=style)
        else:
            result = random_youtube(genre=genre, style=style, year=year)
        
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
                # st.write("")
                with col1:
                    st.write(f"[Discogs Release Page]({link})")
                    st.write(f"[YouTube Search Results]({url})")  
                    st.write(f"#### {title}")
                    if image:
                        st.image(image, use_container_width=True)
                    else:
                        st.image("image/vinyl_discogs.jpg")
                    # if youtube_results:
                    #     st.warning("Most Relevant Youtube Video >>>")
                with col2:
                    if youtube_results:
                        st.warning("Most Relevant Youtube Video >>>")
                    # Gestion des vidéos
                    if discogs_videos:
                        st.video(discogs_videos)
                    elif youtube_results and len(youtube_results) > 0:
                        st.video(youtube_results[0]['url'])
                    else:
                        st.warning(f"No video found for this release. Try [YouTube Search Results]({url})")

            else:
                st.warning("No results found. Try a different selection.")


                
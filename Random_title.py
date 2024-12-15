
#Import
import streamlit as st
import pandas as pd
import requests
import discogs_client
import operator
import csv
import pprint
import random
from utils import d,random_style_album



#>>>>>>>>>>>>>>>>>>>>> Streamlit page


st.set_page_config(
    page_title="JO Paris 2024",
    page_icon="🏅",
    layout="wide",
    initial_sidebar_state="expanded",
)

#>>>>>>>>>>>>>>>>>>>>>> Streamlit sidebar


with st.sidebar:
    st.logo("images/The_Phryges.svg.png")
    st.image("./images/logo-paris-2024.png")

random_style_album("","Italo-Disco",1982)

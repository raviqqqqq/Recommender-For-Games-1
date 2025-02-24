import streamlit as st
import sys

# Setting path to parent Folder
sys.path.append('../ETDS Project')
from filter_recommender_script import recommend_game

#Page config
st.set_page_config(
        page_title="Game Recommender",
        layout="wide",
    )

#Page data
st.markdown("""# Filter System""")

st.markdown("""This app allows you to get recommendations to the Steam titles that you provide or the filter selected. However, the articles may take some time to load, and the data is not up to date.""")

#Taking keyword to search news by
title = st.text_input("Enter the title of the game",key = "title")

#Creating 2 sections for user inputs
col1, col2 = st.columns(2)
with col1:
    selected_category = st.multiselect(
        "Select a category",
        ['None', 'Single-player', 'Family Sharing', 'Multi-player', 'Co-op', 'PvP', 'Shared/Split Screen',
         'Includes level editor', 'Remote Play Together', 'Steam Cloud', 'Full controller support', 'HDR available',
         'Tracked Controller Support', 'VR', 'Online PvP', 'Partial Controller Support', 'MMO', 'Cross-Platform Multiplayer',
         'LAN Co-op', 'Remote Play on TV', 'VR Supported', 'Commentary available', 'Includes Source SDK', 'Mods'],
        key='category'
    )

with col2:
    selected_genre = st.multiselect(
        "Select a genre",
        ['None', 'Casual', 'Indie', 'Action', 'Adventure', 'RPG', 'Strategy', 'Early Access', 'Simulation', 'Racing',
         'Massively Multiplayer', 'Sports', 'Free To Play', 'Design & Illustration', 'Photo Editing', 'Utilities',
         'Video Production', 'Game Development', 'Animation & Modeling', 'Audio Production', 'Software Training',
         'Web Publishing', 'Education', 'Accounting', 'Violent', 'Gore', 'Sexual Content', 'Nudity', 'Movie',
         'Documentary', 'Episodic', 'Short', 'Tutorial', '360 Video'],
        key='genre'
    )

# when button search is clicked
if st.button("Search!"):
    df_result = recommend_game(title, selected_category, selected_genre)

  # this below case will only hit when user selects none in option and title is empty 
  # or we give default values to options (genre and catogary ) when title is empty
    if df_result is None: 
        st.write('Please provide some input!')
    else:
        st.dataframe(df_result)

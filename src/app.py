'''Simple recommendation system for anime titles using content based filtering & Streamlit'''

# Standard library import
from pathlib import Path
from typing import Optional

# Third party imports
import pandas as pd
import streamlit as st

################################################################
# Data loading and preparation

# Get path
path = Path(__file__).resolve().parent

# Root is one level above this file
project_root = path.parent

# Construct data path
data_dir = f'{project_root}/data'

# Load the data
ANIMES_DF = pd.read_parquet(f'{data_dir}/processed_animes.parquet')

# Convert genre strings to sets for easier comparison
ANIMES_DF['genre_set'] = ANIMES_DF['genre'].fillna('').apply(lambda x: set(x.split(', ')))

################################################################
# Helper functions

def get_anime_name(anime_id) -> Optional[str]:
    """Get anime name from ID, returns string or None"""

    global ANIMES_DF

    result = ANIMES_DF[ANIMES_DF['anime_id'] == anime_id]['name']

    return result.values[0] if len(result) > 0 else None


def get_anime_id(anime_name) -> Optional[int]:
    """Get anime ID from name. Returns int or None"""

    global ANIMES_DF

    result = ANIMES_DF[ANIMES_DF['name'] == anime_name]['anime_id']

    return result.values[0] if len(result) > 0 else None


def genre_similarity(genres1, genres2) -> float:
    """Calculates and returns Jaccard similarity between two genre sets."""

    # Return 0 if either set is empty
    if len(genres1) == 0 or len(genres2) == 0:
        return 0

    # Calculate intersection (common genres) and union (all unique genres)
    intersection = len(genres1.intersection(genres2))
    union = len(genres1.union(genres2))

    # Jaccard similarity = intersection / union
    return intersection / union if union > 0 else 0.0


def get_anime_recommendations(target_anime_name: str) -> pd.DataFrame:
    '''Takes an anime title string as input, returns top 5 most similar
    animes based on genera as Pandas dataframe.'''

    # Look up target id from string title
    target_anime_id = get_anime_id(target_anime_name)

    # Select target anime record by id, get geners
    target_anime = ANIMES_DF[ANIMES_DF['anime_id'] == target_anime_id].iloc[0]
    target_genres = target_anime['genre_set']

    print(f"Target anime: {target_anime['name']}")
    print(f"Genres: {target_anime['genre']}")

    # Calculate Jaccard similarity between target and all other animes
    ANIMES_DF['similarity'] = ANIMES_DF['genre_set'].apply(
        lambda x: genre_similarity(target_genres, x)
    )

    # Return the top 5 most similar animes in decending order of 
    # similarity, excluding the target
    similar_animes = ANIMES_DF[ANIMES_DF['anime_id'] != target_anime_id].sort_values(
        'similarity', 
        ascending=False
    )[['name', 'genre', 'similarity']].head(5)

    return similar_animes

################################################################
# Main Streamlit app

if __name__ == '__main__':

    # Set page title
    st.title('Anime recommender')

    # Get target title from user
    anime_title = st.selectbox('Title', ANIMES_DF['name'])

    # Get recommendations
    similar_animes = get_anime_recommendations(anime_title)

    # Index from 1 for user freindly display
    similar_animes.index = list(range(1, len(similar_animes) + 1))

    # Display result
    st.write(similar_animes)


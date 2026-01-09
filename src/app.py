'''Simple recommendation system for anime titles using content based filtering & Streamlit'''

import pandas as pd
import streamlit as st

# Load the data
ANIMES_DF = pd.read_parquet('../data/processed_animes.parquet')

# Convert genre strings to sets for easier comparison
ANIMES_DF['genre_set'] = ANIMES_DF['genre'].fillna('').apply(lambda x: set(x.split(', ')))

def genre_similarity(genres1, genres2):
    """Calculate Jaccard similarity between two genre sets"""

    # Return 0 if either set is empty
    if len(genres1) == 0 or len(genres2) == 0:
        return 0

    # Calculate intersection (common genres) and union (all unique genres)
    intersection = len(genres1.intersection(genres2))
    union = len(genres1.union(genres2))

    # Jaccard similarity = intersection / union
    return intersection / union if union > 0 else 0


def get_anime_recommendations(target_anime_id: int):
    '''Takes an anime as input, returns top 5 most similar
    animes based on genera.'''

    target_anime = ANIMES_DF[ANIMES_DF['anime_id'] == target_anime_id].iloc[0]
    target_genres = target_anime['genre_set']

    print(f"Target anime: {target_anime['name']}")
    print(f"Genres: {target_anime['genre']}")

    ANIMES_DF['similarity'] = ANIMES_DF['genre_set'].apply(
        lambda x: genre_similarity(target_genres, x)
    )

    similar_animes = ANIMES_DF[ANIMES_DF['anime_id'] != target_anime_id].sort_values(
        'similarity', 
        ascending=False
    )[['name', 'genre', 'similarity']].head(5)

    return similar_animes


if __name__ == '__main__':


    st.title('Anime movie recommender')

    anime_number = st.number_input('Input the anime number')

    similar_animes = get_anime_recommendations(int(anime_number))

    st.write(similar_animes)


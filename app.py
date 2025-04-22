# app.py

import streamlit as st
import pickle
import pandas as pd
import requests

# --- Load saved models and data ---
st.header('🎬 Finding a Movie?')

movies = pickle.load(open('movies_cleaned.pkl', 'rb'))
tfidf = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))
tfidf_matrix = pickle.load(open('tfidf_matrix.pkl', 'rb'))
model_knn = pickle.load(open('knn_model.pkl', 'rb'))

# --- Poster fetching ---
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
    return "https://via.placeholder.com/500x750?text=No+Image"

# --- Recommendation using precomputed KNN ---
def recommend(movie_title, n=5):
    try:
        movie_index = movies[movies['title'] == movie_title].index[0]
    except IndexError:
        return [], []

    distances, indices = model_knn.kneighbors(tfidf_matrix[movie_index], n_neighbors=n+1)

    recommended_names = []
    recommended_posters = []
    for i in indices[0][1:]:
        movie_id = movies.iloc[i].movie_id
        title = movies.iloc[i].title
        recommended_names.append(title)
        recommended_posters.append(fetch_poster(movie_id))
    
    return recommended_names, recommended_posters

# --- UI ---
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Let us know your taste! Type or select a movie you like from the dropdown:",
    movie_list
)

if st.button('Show Recommendation'):
    with st.spinner("Finding your next favorite movie..."):
        names, posters = recommend(selected_movie)

        cols = st.columns(5)
        for i, col in enumerate(cols):
            with col:
                st.image(posters[i])
                st.text(names[i])
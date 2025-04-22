# 🎬 Movie-Mate #

A content-based movie recommender app built with Python and Streamlit. It suggests similar movies based on plot, genre, cast, keywords, and director, with posters pulled from the TMDb API.
Check it out here!
https://movie-mate-miapham.streamlit.app/


### **Features** ##
- Suggests 5 similar movies for any selected title
- Uses TF-IDF + KNN (cosine similarity) for recommendations
- Fetches and displays real-time movie posters
- Interactive deployed web app interface with Streamlit


### **Project Files** ###
- movie_recommendation_system.ipynb: Data processing & model training
- app.py: Streamlit web app
- .pkl files: Saved vectorizer, model, and cleaned data


### **How I built this project** ###
1. Preprocessing: Merges movies and credits datasets. Cleans and combines text into a single tags column.
2. Modeling:
- Uses TfidfVectorizer to vectorize tags
- Trains KNN with cosine similarity
3. App: User selects a movie, and the app shows 5 similar titles with posters via the TMDb API.


### **Setup** ###
1. pip install pandas numpy scikit-learn streamlit requests
2. streamlit run app.py
3. Replace the hardcoded TMDb API key in app.py with your own.




Author: Mia Pham



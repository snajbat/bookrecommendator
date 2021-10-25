import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity 
import streamlit as st

df = pd.read_csv("../data_processing/data/the_data.csv")
vectorizer = TfidfVectorizer()

def recommend(book):
    X = vectorizer.fit_transform(df["combined_features"])
    libro = df[df["book_title"] == book]
    if libro.shape[0] == 0:
        st.subheader("Book not found")
        st.text("Check out this insteresting books.")
        return df.sample(15)
    else:
        selected_book = vectorizer.transform(libro["combined_features"])
        cosine_sim = cosine_similarity(X, selected_book)
        recommended = df.copy()
        recommended["sim"] = cosine_sim.sum(axis=-1)
        return recommended.sort_values("sim", ascending=False)[recommended["book_title"] != book].drop_duplicates(subset="book_title").head(15)

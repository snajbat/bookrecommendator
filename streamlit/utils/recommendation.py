import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity 

df = pd.read_csv("../../data_processing/data/the_data.csv")
vectorizer = TfidfVectorizer()

def recommend(book):
    X = vectorizer.fit_transform(df["combined_features"])
    libro = df[df["book_title"] == book]
    selected_book = vectorizer.transform(libro["combined_features"])
    cosine_sim = cosine_similarity(X, selected_book)
    recommend = df.copy()
    recommend["sim"] = cosine_sim.sum(axis=-1)
     return recommend.sort_values("sim", ascending=False)[recommend["book_title"] != book].drop_duplicates(subset="book_title").head(10)

import streamlit as st
from utils.recommendation import recommend

st.title("Book recommendation system")
st.subheader("Select your book and enjoy!")

st.text("")
book = st.text_input("Book title in lowercase")
recommended_books = recommend(book)
recommended_books = recommended_books[["book_title", "image_url"]]

if book:
    columns1 = st.columns(5)
    columns2 = st.columns(5)
    for i in range(5):
        columns[i].image(recommended_books["image_url"][i])
    for i in range(5,10):
        columns2[i-5].image(recommended_books["image_url"][i])
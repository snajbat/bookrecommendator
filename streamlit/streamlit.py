import streamlit as st
from utils.recommendation import recommend

st.title("Book recommendation system")
st.subheader("Select your book and enjoy!")

st.text("")
book = st.text_input("Enter the name of a book you like")


if book:
    recommended_books = recommend(book)
    recommended_books = recommended_books[["book_title", "image_url"]]
    columns = st.columns(5)
    n = 0
    for x in range(5):
        for i in range(n, n+3):
            image = recommended_books["image_url"].iloc()[i]
            if type(image) == str:
                columns[x].image(image)
            columns[x].text(recommended_books["book_title"].iloc()[i])
        n += 3
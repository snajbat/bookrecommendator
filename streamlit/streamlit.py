import streamlit as st
from utils.recommendation import recommend

col1, col2 = st.columns([6,1])
with col1:
    st.title("Book recommendation system")
with col2:
    st.image("https://p.kindpng.com/picc/s/293-2934582_from-the-blog-logo-book-black-png-transparent.png", width=100)

st.markdown("<h4 style='text-align: center;'>Select your book and enjoy!</h4>", unsafe_allow_html=True)


st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
book = st.text_input("Enter the title of a book you like with the first letter of each word capitalized and press Enter.")


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
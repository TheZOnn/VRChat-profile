import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png')

with col2:
    title = """
    Hi, I'm the TheZOnn
    """
    st.title(title)
    content = """
    I also go by the names: Verizon, Verizonn and Zazoon.
    I'm a little goober that goofs around the internet sometimes. I created this website so it could be some random 
    portfolio that I doubt I would use in the future.
    """
    st.info(content)

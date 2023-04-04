import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)


with col1:
    st.image('images/photo.PNG')
    st.write('A little profile drawing that one of my friends made')

with col2:
    title = """
    Yo, I'm the TheZOnn
    """
    st.title(title)
    image_stucker = """
    I also go by the names: Verizon, Verizonn and Zazoon.\n
    Currently learning the ropes of web development and all of that and I made this using Streamlit and Python\n
    Thanks for reading this, so come say hi!
    """
    st.info(image_stucker)

mainbody1 = """VRChat collage"""
st.title(mainbody1)
st.write("""
A little collage of some noteworthy VRChat moments with me and some cool people
""")

col3, col4 = st.columns(2)

with col3:
    st.image('vrmoments/vr1.png')
    st.image('vrmoments/vr2.png')

with col4:
    st.image('vrmoments/vr3.png', width=442)
    st.image('vrmoments/vr4.png', width=442)




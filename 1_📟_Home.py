import streamlit as st
from PIL import Image
import requests

st.set_page_config(page_title="Home", page_icon='📟')

a1 = Image.open("images/pic2.png")
a2 = Image.open("images/pic1.png")

st.title("RUMOR - A NLP Content Creation Tool")
st.write("Rumor helps the user to get many different functionalities with a single prompt.")

with st.container():
    st.write("---")
    left_col1, right_col1 = st.columns(2)
    with left_col1:
        st.image(a2, width=250)
    with right_col1:
        st.subheader("What is Rumor? ")
        st.write("Rumor is a smart application that offers a streamlined and user-friendly approach for a person to generate and enter the text/prompt of their liking and select the services accordingly and see the magic happen.")
        
with st.container():
    st.write("---")
    st.header("Services:")
    left_col2, right_col2 = st.columns(2)
    with left_col2:
        with st.expander("1. Text Generator"):
            st.write("Capable of generating text from a given text")
        with st.expander("2. Text Sumarization"):
            st.write("Capable of Summarizing long text")
        with st.expander("3. Sentiment Analysis"):
            st.write("Capable of predicting the sentiment of a text")
        with st.expander("4. Grammer Corrector"):
            st.write("Capable of cheking and correcting the grammar of a text")
    with right_col2:
        st.image(a1, width=300)

if(st.button("Go to Services")):
   st.switch_page("pages/2_💻_Services.py") 
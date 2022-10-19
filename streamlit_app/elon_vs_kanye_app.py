# -*- coding: utf-8 -*-
from PIL import Image

import streamlit as st
import pandas as pd
import requests

import plotly.express as px

title_image = Image.open('./elon_and_kanye.jpeg')
st.image(title_image, width=400)
st.title("Who tweeted this: Elon or Kanye?")
st.text("")
st.text("")
st.text("")
# st.markdown("Elon or Kanye?")

# @st.cache(persist=True)
# def load_data():
    # df = pd.read_csv("https://datahub.io/machine-learning/iris/r/iris.csv")
    # return(df)

def run():
    # st.subheader("Iris Data Loaded into a Pandas Dataframe.")
    # tweet = st.text_input('Input your tweet here')

    if st.button('Check for new mystery tweet!'):
        tweet_data = requests.post(f"https://newsreader-test2-nygqre3mjq-uc.a.run.app")
        if tweet_data:
            if tweet_data['prediction'] == "elon":
                image = Image.open('./elon.jpeg')
            else:
                image = Image.open('./kanye.jpg')

            col1, col2 = st.columns(2)

            with col1:
                st.markdown(tweet_data['tweet'], unsafe_allow_html=False)
            with col2:
                st.image(image, caption='This is our mystery tweeter.')
    
if __name__ == '__main__':
    run()    

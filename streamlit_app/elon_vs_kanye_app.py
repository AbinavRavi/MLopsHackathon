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
# st.markdown("Elon or Kanye?")

# @st.cache(persist=True)
# def load_data():
    # df = pd.read_csv("https://datahub.io/machine-learning/iris/r/iris.csv")
    # return(df)

# Twitter Account Name: @MMlopsss

def run():
    # st.subheader("Iris Data Loaded into a Pandas Dataframe.")


    tweeter_handle = st.text_input('Input username of myster twitter user here.')
    if st.button('Check for new mystery tweet!'):

        bearer_token = "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImVlMWI5Zjg4Y2ZlMzE1MWRkZDI4NGE2MWJmOGNlY2Y2NTliMTMwY2YiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiIzMjU1NTk0MDU1OS5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsImF1ZCI6IjMyNTU1OTQwNTU5LmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwic3ViIjoiMTE3NTIyNTg5NTk0ODU2NDU4NjE5IiwiZW1haWwiOiJmbG9rZGVAZ29vZ2xlbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXRfaGFzaCI6Ikc4dkxmakxuN3NfSkpPTmV5cEduQVEiLCJpYXQiOjE2NjYyMDUwNTUsImV4cCI6MTY2NjIwODY1NX0.X0yl-RmBXVaA-xdX6wX2AzzaY4sRAuZ09bwTkAEImC0Vtkah0SNTSsvza-vGy1B_Z6sdfEvJV2q69yMO2H3uDdafZeet3idRyJvZwbUsiYNAUrC3ZFG_nWn6-JqhThfZ-ktrlgKEGlCDdBJAGyHZQfHBzOQgoCK2E5UfKpQUFN5N0hk0i4RCFc4f0sRG_SmHzaDLxgnSFAEKklIqk0UZhahA7vouBEJqbdj7cMpLa4m8L8LhMDUeik8erKQ_5e4YudqPkcMAzZ1MRLyDuIVH4cBL-EeXdU-xCga9sv6BEdOu3fMCMatmskweKSNkeg4Ga0Ih6r-TKAvs7SwbahqRIg"

        header = {
                'Authorization': bearer_token,
                'content_type': 'application/json',
                }
        
        data = {
                'accounts': [tweeter_handle],
                'dest': 'live_elon_kanye1.tweets1',
                }

        tweet_data = requests.post("https://newsreader-test2-nygqre3mjq-uc.a.run.app/twitter", headers=header, json=data)

        print(tweet_data)

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

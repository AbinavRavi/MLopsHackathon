# -*- coding: utf-8 -*-
from PIL import Image
import streamlit as st
import requests
from fastapi import FastAPI
from pydantic import BaseModel

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

        bearer_token = "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImVlMWI5Zjg4Y2ZlMzE1MWRkZDI4NGE2MWJmOGNlY2Y2NTliMTMwY2YiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiIzMjU1NTk0MDU1OS5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsImF1ZCI6IjMyNTU1OTQwNTU5LmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwic3ViIjoiMTE3NTIyNTg5NTk0ODU2NDU4NjE5IiwiZW1haWwiOiJmbG9rZGVAZ29vZ2xlbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXRfaGFzaCI6ImVGNjFWLS1JdHpRVzJBZXpQX0x3NlEiLCJpYXQiOjE2NjYyMDk0OTgsImV4cCI6MTY2NjIxMzA5OH0.PO3kX9NwQaotYVGZRoVz0JSSHcb3E_GTh3bvmvwLf0ZDHfnkZrx1WkrGWr9eLbP-gZ2zRi_4UZYB97d4aULoUJwEsKVc-4umknTM6NQT3wk6DqtMcLqb7W-u8YqOHBqDESRQooVq1WTb0nIFJa1Dotls9u_DiQUXGz5sZP4xv_NWb4PWvyNwoSxBhAqx65TqYLpvBiB5vvDLI_8ZswP0951QwWA1Ah6lwoRSeXnr-dpd7PVKdr2luuYksopf4L4hQs7p330InkzoD350a8XXhDQlDrGiTl-OoaopM3cNDxQCiNxnjyIq1t69uVfS2uDiy9XuaeW--MKFbGZyZF_tdA"

        header = {
                'Authorization': bearer_token,
                'content_type': 'application/json',
                }
        
        data = {
                'accounts': [tweeter_handle],
                'dest': 'live_elon_kanye1.tweets3',
                'limits': 5,
                }

        tweet_data = requests.post("https://newsreader-test2-nygqre3mjq-uc.a.run.app/twitter", headers=header, json=data)


def inference():
    tweet_data_fake = {
            'prediction': 'elon',
            'tweet': 'Doge to the moon!'
            }

    if tweet_data_fake:
        if tweet_data_fake['prediction'] == "elon":
            image = Image.open('./elon.jpeg')
        else:
            image = Image.open('./kanye.jpg')

        # col1, col2 = st.columns(2)

        # with col1:
            # st.markdown(tweet_data_fake['tweet'], unsafe_allow_html=False)
        # with col2:
            # st.image(image, caption='This is our mystery tweeter.')
        st.markdown(tweet_data_fake['tweet'], unsafe_allow_html=False)
        st.image(image, caption='This is our mystery tweeter.')

if __name__ == '__main__':
    run()
    inference()

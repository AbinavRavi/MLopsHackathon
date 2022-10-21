# -*- coding: utf-8 -*-
from PIL import Image
import streamlit as st
import requests

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

        bearer_token = "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImVlMWI5Zjg4Y2ZlMzE1MWRkZDI4NGE2MWJmOGNlY2Y2NTliMTMwY2YiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiIzMjU1NTk0MDU1OS5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsImF1ZCI6IjMyNTU1OTQwNTU5LmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwic3ViIjoiMTE3NTIyNTg5NTk0ODU2NDU4NjE5IiwiZW1haWwiOiJmbG9rZGVAZ29vZ2xlbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXRfaGFzaCI6InhQSUplTEM1UmN3RFZlVGg2SGhCX2ciLCJpYXQiOjE2NjYyNTYzODYsImV4cCI6MTY2NjI1OTk4Nn0.pLpAoND9sz8naMpHmoMXM1yiSvVw1PpnN7zhMv184G1ah3OhZv_H1N1rMLYFKh6X7ux_9yc1MkAV2Z3icjjI9G4nPg5Xleij3Jb07weVDppwFSwUt95YgoYNTfSJ4lELhuamTrq6rLIu66Kvi7HRjMctEFrnyY74w7CrFUBpgCZquH-4Ssd4pgqXsW_UJE748Z-5Kc7kvlF3Thwt9ek5vc_iyKuSzDYQhNjwIu5J4NjXiIE7HGTfzXfhrLM4jfIP3NTH8ttelC65F3fdIrLNxRxqmJC4NW9GAZa2hcDAI5pPuq_JwVBkXFFHzrsEqpyRmBOiYOpnpA-ZY0AJV2J1Gw"

        header = {
                'Authorization': bearer_token,
                'content_type': 'application/json',
                }
        
        data = {
                'accounts': [tweeter_handle],
                'dest': 'live_elon_kanye1.tweets7',
                'limits': 5,
                }

        tweet_data = requests.post("https://newsreader-test2-nygqre3mjq-uc.a.run.app/twitter", headers=header, json=data)

        print(tweet_data)

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

import streamlit as st
import requests

# App Header
st.title("Movie Picker Frontend")

st.markdown('''
This app allows you to input movie name and retrieve movie suggestions using an API.
''')

# Input Parameters
st.sidebar.header("Input Parameters")
input = st.sidebar.text_input("Movie Name", "Parasite")
type = st.sidebar.text_input("Search Type", "name")


# API Endpoint
url = 'https://moviepicker-503519505843.europe-west1.run.app/predict'

# Create API Request Payload
payload = {
    "key": "test",
    "input": input,
    "type": type,
}

# Call the API
if st.button("Get Movie Suggestion"):
    try:
        response = requests.get(url, params=payload)
        if response.status_code == 200:
            prediction = response.json()
            st.success(f"Movie Suggestions: {prediction}")
        else:
            st.error(f"API call failed! Status code: {response.status_code}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# import streamlit as st
# import numpy as np
# import pandas as pd
# st.markdown("""# Movie Recommender
# ## Have you ever scrolled on Netflix to find a new movie and searched for so long… ?
# We’ve got the solution!""")
# st.write(“Choose a movie :”)
# input = st.text_input('Movie title')
# str.write(”Which one did you mean ?”)
# find_movies(input)
# line_count = st.slider('Choose the number of movies recommendations', 1, 10, 5)
# predict(input, name)

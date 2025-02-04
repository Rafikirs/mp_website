import streamlit as st
import requests


# App Header
# st.title("Movie Picker Frontend")

# st.markdown('''
# This app allows you to input movie name and retrieve movie suggestions using an API.
# ''')


st.title("Movie Picker")
st.markdown("<h1 style='font-size: 26px;'>Tired of scrolling on streaming platforms to find a movie you don't even like ?</h1>", unsafe_allow_html=True)
# st.markdown("<h1 style='font-size: 20px;'>We've got the solution !</h1>", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .big-text {
        font-size: 20px !important;
        color: black;
    }
    </style>
    <p class="big-text">We've got the solution !</p>
    """,
    unsafe_allow_html=True
)

st.text("")

# Input Parameters
st.sidebar.header("Input Parameters")
option = st.sidebar.radio("Choose a recommendation method :", ["by Movie Name", "by Filters"])

if option == "by Movie Name":
    st.sidebar.markdown("Find movie recommendations based on a movie you like")
    input = st.sidebar.text_input("Movie Name")

elif option == "by Filters":
    st.sidebar.markdown("Find movie recommendations based on genre, language and/or description")
    st.sidebar.selectbox('Movie Genre', [])
    st.sidebar.selectbox('Movie Language', [])
    st.sidebar.text_input('Movie description')


# API Endpoints
url1 = 'https://moviepicker-503519505843.europe-west1.run.app/find'
url2 = 'https://moviepicker-503519505843.europe-west1.run.app/predict'
url3 = 'https://moviepicker-503519505843.europe-west1.run.app/get_image'
url4 = 'https://moviepicker-503519505843.europe-west1.run.app/get_url'
url5 = 'https://moviepicker-503519505843.europe-west1.run.app/get_description'

# API Endpoints
# url1 = 'http://localhost:8000/find'
# url2 = 'http://localhost:8000/predict'
# url3 = 'http://localhost:8000/get_image'
# url4 = 'http://localhost:8000/get_url'
# url5 = 'http://localhost:8000/get_description'


if option == "by Movie Name":
    # Find movies with an input name
    find_params = {
    "input_name": input,
    "dataset_choice" : "final"
    }

    find_response = requests.get(url1, params=find_params)

    if find_response.status_code == 200:
        found_movies = find_response.json()
        if found_movies == [] and input != "":
            st.error(f"This movie can't be found!")
        else:
            right_movie = st.selectbox('Which movie did you mean ?', found_movies) # Ask user to choose the right movie


# Ask user how many reco he wants
n_recommendations = st.slider('How many recommendations do you want ?', 1, 10, 5)


if st.button("Get Movie Suggestions"):

    # Create a space
    st.write("")

    # Get the prediction as a list of movies
    suggestion_params = {
    "input_name" : right_movie,
    "n_recommendations" : n_recommendations
    }

    predict_response = requests.get(url2, params=suggestion_params)
    if predict_response.status_code == 200:
        prediction = predict_response.json()

        # Loop through all movie recommendations
        for movie in prediction:
            # Print the title of the movie
            st.subheader(movie)

            # Print the image of the movie
            image_params = {
            "movie": movie,
            }

            image_response = requests.get(url3, params=image_params)
            if image_response.status_code == 200:
                image = image_response.json()
                if image:
                    st.image(image, width=300)


            # Print the description of the movie
            description_params = {
            "movie": movie
            }

            description_response = requests.get(url5, params=description_params)
            if description_response.status_code == 200:
                description = description_response.json()

                st.markdown(f"**{description}**")

                st.text("")

                st.markdown(
                    f"""
                    <div style="
                        border: 2px solid #4A90E2;
                        padding: 10px;
                        border-radius: 10px;
                        background-color: #F0F8FF;
                        text-align: left;
                        font-size: 15px;
                        font-weight: normal;
                        color: #333;">
                        {description}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.text("")

                st.markdown(
                    f"""
                    <div style="
                        border-left: 5px solid #FF4B4B;
                        padding: 10px;
                        background-color: #222;
                        color: white;
                        font-size: 15px;
                        font-weight: bold;">
                        {description}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.text("")

                st.markdown(
                    f"""
                    <div style="
                        background-color: black;
                        padding: 20px;
                        border-radius: 12px;
                        box-shadow: 0px 4px 10px rgba(255, 255, 255, 0.2);
                        font-size: 15px;
                        font-weight: bold;
                        color: white;">
                        {description}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.text("")

                st.markdown(
                    f"""
                    <div style="
                        background-color: white;
                        padding: 20px;
                        border-radius: 12px;
                        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
                        font-size: 15px;
                        font-weight: bold;
                        color: #0000FF;">  <!-- This is a vibrant blue -->
                        {description}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.text("")

                st.markdown(
                    f"""
                    <div style="
                        background-color: white;
                        padding: 20px;
                        border-radius: 12px;
                        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
                        font-size: 15px;
                        font-weight: bold;
                        color: #333;">
                        {description}
                    </div>
                        """,
                    unsafe_allow_html=True
                )

            # Create a space
            st.write("")

            # Get the Letterboxd url of the movie
            url_params = {
                "movie" : movie
            }
            url_response = requests.get(url4, params=url_params)
            if url_response.status_code == 200:
                url = url_response.json()

            st.markdown(f"[Click here for more information]({url})")

            # Create a space
            st.write("")

    else:
        st.error(f"Sorry, an error occurred.")

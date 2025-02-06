import streamlit as st
import requests

def set_bg_image(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: top;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set the background image (Replace with your image URL)
set_bg_image("https://raw.githubusercontent.com/aybik/mp_website/refs/heads/master/wp3286092.webp")

col1, col2, col3 = st.columns([0.5, 2.7, 0.5])
with col2:
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.title("Movie Picker")

st.markdown("<h1 style='font-size: 26px;'>Tired of scrolling to find your next watch?</h1>", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .big-text {
        font-size: 20px !important;
        color: white;
    }
    </style>
    <p class="big-text">We've got the solution !</p>
    """,
    unsafe_allow_html=True
)

st.text("")

# Input Parameters
st.sidebar.image("logo_panda_2.png", use_container_width=True)
st.sidebar.markdown("<h2 style='text-align: center;'>Input Parameters</h2>", unsafe_allow_html=True)
option = st.sidebar.radio("Choose a recommendation method :", ["by Movie Name", "by Filters"])

if option == "by Movie Name":
    st.sidebar.markdown("Find movie recommendations based on a movie you like")
    input = st.sidebar.text_input("Movie Name")

elif option == "by Filters":
    st.sidebar.markdown("Find movie recommendations based on genre, language and/or description")
    input_genre = st.sidebar.selectbox('Movie Genre', ['action', 'adventure', 'animation', 'comedy', 'crime', 'documentary',
        'drama', 'family', 'fantasy', 'history', 'horror', 'music', 'mystery',
        'romance', 'science_fiction', 'thriller', 'tv_movie', 'war', 'western'], index=0)#, default=['comedy', 'action'])
    input_language = st.sidebar.selectbox('Movie Language', ['English', 'Korean', 'Japanese', 'French', 'German', 'Spanish',
       'Norwegian', 'Cantonese', 'Portuguese', 'Russian', 'Danish',
       'Italian', 'Swedish', 'Greek (modern)', 'Telugu', 'Chinese', 'Icelandic', 'Finnish', 'Indonesian', 'Czech',
       'Persian (Farsi)', 'Polish', 'Dutch', 'Mayan', 'Turkish',
       'Armenian', 'Arabic', 'Thai', 'Irish', 'Hindi',
       'Hebrew (modern)', 'Bengali, Bangla', 'Hungarian', 'Romanian',
       'Serbian', 'Georgian', 'Galician', 'Urdu', 'Macedonian',
       'Estonian', 'Wolof', 'Catalan', 'Swahili', 'Serbo-Croatian',
       'Tagalog', 'Vietnamese', 'Malayalam', 'Ukrainian', 'Kinyarwanda',
       'Tamil', 'Slovak', 'Kurdish', 'Southern Sotho', 'Dzongkha',
       'Welsh', 'Tola', 'Bosnian', 'Croatian', 'Basque', 'Lithuanian',
       'Bambara', 'Kannada', 'Lingala', 'Latin', 'Tswana', 'Malay',
       'Marathi', 'Albanian', 'Sundanese', 'Afrikaans', 'Gujarati', 'Lao',
       'Oromo', 'Pashto, Pushto', 'Yiddish', 'Inuktitut', 'Aymara',
       'No spoken language', 'Assamese', 'Ossetian, Ossetic', 'Akan',
       'Quechua', 'Latvian', 'Bislama', 'Xhosa', 'Mongolian', 'Moldavian',
       'Fula, Fulah, Pulaar, Pular', 'Maltese', 'Yolngu matha', 'Nepali',
       'Esperanto', 'Gibberish', 'Kashmiri', 'Northern Sami', 'Slovene',
       'Amharic', 'Maithili', 'Guaraní',
       'Tibetan Standard, Tibetan, Central', 'Māori', 'Kazakh',
       'Bulgarian', 'Khmer', 'Somali', 'Kyrgyz',
       'Eastern Punjabi, Eastern Panjabi', 'Azerbaijani', 'Burmese',
       'Samoan', 'Javanese', 'Zulu', 'Mari', 'Scottish Gaelic, Gaelic',
       'Sinhalese, Sinhala', 'Hausa', 'Breton', 'Faroese', 'Uzbek',
       'Haitian, Haitian Creole', 'Shona', 'Luxembourgish, Letzeburgesch',
       'Uyghur', 'Chechen', 'Twi', 'Igbo', 'Malagasy', 'Norwegian Bokmål',
       'Belarusian',
       'Old Church Slavonic, Church Slavonic, Old Bulgarian',
       'Sardinian', 'Tajik', 'Turkmen', 'Oriya', 'Southern Ndebele',
       'Cree', 'Abkhaz', 'Kalaallisut, Greenlandic',
       'Limburgish, Limburgan, Limburger', 'Sanskrit (Saṁskṛta)',
       'Chuvash', 'Yoruba', 'Norwegian Nynorsk', 'Afar', 'Sango', 'Ganda',
       'Western Frisian', 'Interlingue', 'Chichewa, Chewa, Nyanja',
       'Tonga (Tonga Islands)', 'Kongo', 'Venda', 'Occitan',
       'Divehi, Dhivehi, Maldivian', 'Marshallese', 'Tigrinya', 'Romansh',
       'Tahitian', 'Northern Ndebele', 'Corsican', 'Tatar', 'Cornish'], index=0)
    input_description = st.sidebar.text_input('Movie description')


# API Endpoints
url1 = 'https://moviepicker-503519505843.europe-west1.run.app/find'
url2 = 'https://moviepicker-503519505843.europe-west1.run.app/predict_name'
url6 = 'https://moviepicker-503519505843.europe-west1.run.app/predict_filter'
url3 = 'https://moviepicker-503519505843.europe-west1.run.app/get_image'
url4 = 'https://moviepicker-503519505843.europe-west1.run.app/get_url'
url5 = 'https://moviepicker-503519505843.europe-west1.run.app/get_description'


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
    with st.container():

        if option == "by Movie Name":
            # Get the prediction as a list of movies
            suggestion_params = {
            "input_name" : right_movie,
            "n_recommendations" : n_recommendations
            }

            predict_response = requests.get(url2, params=suggestion_params)

        elif option == "by Filters":
            suggestion_params = {
            "user_description" : input_description,
            "user_language" : input_language,
            "user_genres": input_genre,
            "n_recommendations" : n_recommendations
            }

            predict_response = requests.get(url6, params=suggestion_params)

        if predict_response.status_code == 200:
            prediction = predict_response.json()

            # Loop through all movie recommendations
            for movie in prediction:
                # Print the title of the movie
                col1, col2 = st.columns([1, 2])  # 1/3 for poster, 2/3 for text
                with col1:
                    # Print the image of the movie
                    image_params = {
                    "movie": movie,
                    }
                    image_response = requests.get(url3, params=image_params)
                    if image_response.status_code == 200:
                        image = image_response.json()
                        if image:
                            st.image(image, width=250)


                # Print the description of the movie
                with col2:
                    st.subheader(movie)
                    description_params = {
                    "movie": movie
                    }

                    description_response = requests.get(url5, params=description_params)
                    description = description_response.json()

                    st.text("")

                    st.markdown(
                        f"""
                        <div style="
                            border: 2px solid #242323;
                            padding: 10px;
                            border-radius: 10px;
                            background-color: #c0c3c4;
                            text-align: left;
                            font-size: 15px;
                            font-weight: normal;
                            color: #333;">
                            {description}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )



                # Get the Letterboxd url of the movie
                url_params = {
                    "movie" : movie
                }
                url_response = requests.get(url4, params=url_params)
                if url_response.status_code == 200:
                    url = url_response.json()
                    st.markdown(f"[🔗 Click here for more information]({url})")

                st.markdown("---")  # Separator between movies

        else:
            st.error(f"Sorry, an error occurred.")

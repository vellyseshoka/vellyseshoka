"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model
import png

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Home","Recommender System","Solution Overview","Exploratory Data Analysis","About"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Home":
        
        st.write('# Movie Recommender Engine')
        st.write('### EDSA Unsupervised Predict Team GM6')
        image = Image.open('resources/imgs/Home-Picture.jpg')
        st.image(image, caption='TEAM GM6', use_column_width=True)
	    # st.image(image name, width = None)
        st.write("Recommendation System is a filtration program whose prime goal is to predict the “rating” or “preference” of a user towards a domain-specific item or item. In our case,"
        "this domain-specific item is a movie,"
        "therefore the main focus of our recommendation system is to filter and predict only those movies which a user would prefer given some data about the user him or herself.")

    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.subheader("Our winning approach")
        st.markdown('We employed two methods of building recommmendation system:')
        st.markdown('#### Content-based filtering & Collaborative filtering')
        st.markdown("The Content-Based Recommendation system computes similarity between movies based on movie genres using the selected movie as a baseline. Using this type of movie recommendation system, we require the title of the movie as input, but our sim_matrix is based on the index of each movie. Therefore, to build this, we need to convert movie title into movie index and movie index into movie title. Let's create functions which operate those functions.")
        st.markdown("Collaborative methods for recommender systems are methods that are based solely on the past interactions recorded between users and items in order to produce new recommendations. These methods do not require item meta-data like their content-based counterparts. This makes them less memory intensive which is a major plus since our dataset is so huge.")
        st.markdown("Our best perfoming solution to a movie recommender sytem was the collaborative filtering. We intergrated it with our best perfoming model which is the SVD model as seen in the graph below.")
        st.subheader('A graph of Model Perfomances')
        st.image('resources/imgs/velly.png',use_column_width=True)
        st.markdown('From the image above the SVD model perfomed best with an RMSE of 0.92 as compared to the other models.')
        st.markdown('The singular value decomposition (SVD) provides another way to factorize a matrix, into singular vectors and singular values. The SVD allows us to discover some of the same kind of information as the eigen decomposition.The SVD is used widely both in the calculation of other matrix operations, such as matrix inverse, but also as a data reduction method in machine learning. SVD can also be used in least squares linear regression, image compression, and denoising data.')



    if page_selection == "Exploratory Data Analysis":

        st.title('EDA')
        if st.checkbox("Movie Production"):
            st.subheader("Movies Produced per Year")
            st.image('resources/imgs/Movies_Produced_Per_Year.png',use_column_width=True)
            st.write("More than 1700 movies were produced in the year 2015, which is the year with the highest numbers of movies produced, followed by the year 2016 and 2017, which both have more than 1500 movies produced")

        if st.checkbox("Genres"):
            st.subheader("Movie Genres")
            st.write("Here we look at Movie genres that appears most in movies. This information will enable us understand the genres of movies produced most for the period the data was captured.")
            st.image('resources/imgs/gengre.png',use_column_width=True)
            st.write("Drama and Comedy are the most popular genres, followed by Thriller and Romance. We need to keep in mind that the movies could have multiple genres.")


        if st.checkbox("Top Watched Movies"):
            st.subheader("Movies That Are Nostly Watched")
            st.image('resources/imgs/wordcloud.png',use_column_width=True)
            st.write("We can see from the wordcloud that Sci-Fi, Action, Adventure, Drama and Crime are the top watched Genres movies.")


    if page_selection == "About":

        
        left_column, right_column = st.columns(2)
        with right_column:
            st.info("### MovieS!x App Developers")
            st.info("Contact details in case you have any query")
            st.write("---")
            st.write("Gomolemo : Gomolemo@gmail.com")
            st.write("Abigail : Abigail@gmail.com")
            st.write("Aphiwe : Aphiwe@gmail.com")
            st.write("Zothandwa : Zothandwa@gmail.com")
            st.write("Mapule : Mapule@gmail.com")
            st.write("Velly : Velly@gmail.com")

            st.markdown(""" 
		For more info:
		email: moreinfo@MovieS!X.com
		""")
        with left_column:

            mail = Image.open('resources/imgs/Presentation.png')
            st.image(mail, width = None)

            mail2 = Image.open('resources/imgs/email2.png')
            st.image(mail2, width = None)

    # or to provide your business pitch.


if __name__ == '__main__':
    main()

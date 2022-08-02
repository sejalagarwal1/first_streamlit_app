import streamlit
import pandas
#importing pandas lib to make table
streamlit.title('my parents healthy new dinner')
streamlit.header('Breakfast favorties')
streamlit.text('🥣Omega3 and buleberry Oat meal')
streamlit.text('🥗Kale, spinach and Rocket smoothie')
streamlit.text('🐔Hard-boiled free-range egg')
streamlit.text('🥑🍞Avacodo Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#reading the file from s3 bucket
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

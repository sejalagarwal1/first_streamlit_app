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
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

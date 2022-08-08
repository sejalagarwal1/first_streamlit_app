import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
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
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#creating function
def get_fruitvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  # take the json version of the response and normalise it
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

#adding a section for fruitvice api response
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
  else:
    back_from_function=get_fruitvice_data(fruit_choice)
    # output it in the screen as table
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()
    
#starting with snowfalke connector
streamlit.header("The fruit load list contains:")
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur
  my_cur.execute("SELECT * from fruit_load_list")
  retun my_cur.fetchall()

#adding button to load data
if streamlit.button('get fruit list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)
  
streamlit.stop()

#adding another user input
add_my_fruit = streamlit.text_input('What fruit would you like to add?','Jackfruit')
streamlit.write('Thanks for adding ', add_my_fruit)

my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")

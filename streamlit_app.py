# Lesson 3

import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error  import URLError


streamlit.title('My Parents New Healthy Dinner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]


#Display the table on the page
streamlit.dataframe(fruits_to_show)


#New Section to display fruityvice response
streamlit.header('Fruityvice Fruit Advice!')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
      streamlit.error("Please select a fruit to get information.")
  else:
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      streamlit.dataframe(fruityvice_normalized)
except URLEroor as e:
    streamlit.error()


#Donot run anything past here while we trouble shoot
streamlit.stop()



my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)




#Add a second text box
# streamlit.header('What would you like to add!')
add_my_fruit = streamlit.text_input('What would you like to add?', 'jackfruit')
streamlit.write('Thanks for adding', add_my_fruit)

fruityvice_add = requests.get("https://fruityvice.com/api/fruit/" + add_my_fruit)

#take the json version of the add and normalize it
fruityvice_normalized2 = pandas.json_normalize(fruityvice_add.json())
# output it the screen as a table
streamlit.dataframe(fruityvice_normalized2)

#This will not work correctly, but just go with it for now
my_cur.execute("insert into fruit_load_list values('from streamlit')")









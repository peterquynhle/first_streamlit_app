# Lesson 3

import streamlit

streamlit.title('My Parents New Healthy Dinner')

streamlit.header(' Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑 🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

# Choose the Fruit Name Column as the Index
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's Create Some User Interaction

# let  put a piclk ist here so the can  pick the fruitthey want to include:
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]


# Display the table on the page.
streamlit.dataframe(fruits_to_show)

# Lesson 9
#Let's Call the Fruityvice API from Our Streamlit App!

# New section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon"+ fruit_choice)
# comment out this line to remove json data from the app: "streamlit.text(fruityvice_response.json())"

#🥋 Making the JSON Look Good
#take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

#Output it in the screen as a table
streamlit.dataframe(fruityvice_normalized)



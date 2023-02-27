import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os
import matplotlib.pyplot as plt
import folium


# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "cities.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "mega_cities.csv")

st.title("Mega City Visualization Dashboard")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)




# Create a dropdown menu to select a country
Country = st.selectbox('Select a country:', df['country'].unique())

# Filter the dataset based on the selected country
filtered_data = df[df['country'] == Country]

# Create a bar chart of the population of each city in the selected country
fig = px.bar(filtered_data, x='mega_city', y='population', labels={'x': 'City', 'y': 'Population'})
fig.update_layout(title=f'Population of Cities in {Country}')
st.plotly_chart(fig)

#Create a bar chart of the top 10 most populous cities
top_cities = df.sort_values('population', ascending=False).head(10)
fig = px.bar(top_cities, x='mega_city', y='population', labels={'x': 'City', 'y': 'Population'})
fig.update_layout(title='Top 10 Most Populous Cities')
st.plotly_chart(fig)

# Group the data by country and sum the population
country_data = df.groupby('country')['population'].sum().reset_index()

# Create a pie chart of the total population for each country
fig = px.pie(country_data, values='population', names='country', title='Total Population by Country')
st.plotly_chart(fig)
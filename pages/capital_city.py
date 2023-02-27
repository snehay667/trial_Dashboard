import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os
import matplotlib.pyplot as plt
import seaborn as sns


# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "city.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "capital_cities.csv")

st.title("Capital City Visualization Dashboard")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

Countries = st.selectbox("Select the Continent:", df['continent'].unique())

col1, col2 = st.columns(2)

# Create a histogram of the capital population for the selected continent
fig_1 = px.histogram(df[df['continent'] == Countries], x="capital_population")

# Create a box plot of the capital population for the selected continent
fig_2 = px.box(df[df['continent'] == Countries], y="capital_population")

# Display the histogram and the box plot
col1.plotly_chart(fig_1, use_container_width=True)
col2.plotly_chart(fig_2, use_container_width=True)

# Group the data by continent and sum the population
grouped_data = df.groupby("continent").agg({"capital_population": "sum"}).reset_index()
# Create the pie chart
fig = px.pie(grouped_data, values="capital_population", names="continent")
# Display the chart
st.plotly_chart(fig)

# Create a selectbox to allow the user to choose a continent
continent = st.selectbox('Select a Continent:', df['continent'].unique())

# Filter the data by continent
filtered_data = df[df['continent'] == continent]

# Create a scatter plot of capital city population versus continent
fig = px.scatter(filtered_data, x='continent', y='capital_population', title=f'Capital City Population in {continent}')
st.plotly_chart(fig)




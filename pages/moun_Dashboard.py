import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os
import matplotlib.pyplot as plt


# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "moun.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "mountainranges.csv")

st.title("Dashboard - Moun Data")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

Countries = st.selectbox("Select the Countries:", df['countries'].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['countries'] == Countries], x="height")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['countries'] == Countries], y="height")
col2.plotly_chart(fig_2, use_container_width=True)

   


# Create a bar chart of the highest mountain in each mountain range
highest_mount = df.groupby('mountain_range')['highest_mount'].max().sort_values()
fig1 = px.bar(highest_mount, x=highest_mount.index, y=highest_mount.values, labels={'x': 'Mountain Range', 'y': 'Height (m)'})
fig1.update_layout(title='Highest Mountain in Each Mountain Range')
st.plotly_chart(fig1)

# Create a scatter plot of the relationship between the height of the mountain range and the highest mountain in that range
fig2 = px.scatter(df, x='height', y='highest_mount', color='mountain_range')
fig2.update_layout(title='Relationship Between Height of Mountain Range and Height of Highest Mountain')
st.plotly_chart(fig2)

# Create a table of the top 10 mountain ranges by highest mountain
top_ranges = df.sort_values('highest_mount', ascending=False).groupby('mountain_range').first().head(10)
st.subheader('Top 10 Mountain Ranges by Highest Mountain')
st.table(top_ranges)



# Create a pie chart of the distribution of mountain ranges across different countries
countries = df.groupby('countries')['mountain_range'].nunique().sort_values()
fig3 = px.pie(names=countries.index, values=countries.values)
fig3.update_layout(title='Distribution of Mountain Ranges Across Different Countries')
st.plotly_chart(fig3)



# Create a dropdown menu to select a country
country = st.selectbox('Select a country:', df['countries'].unique())

# Filter the dataset based on the selected country
filtered_data = df[df['countries'] == country]

# Display a bar chart of the highest mountain in each mountain range in the selected country
fig = px.bar(filtered_data, x='mountain_range', y='highest_mount', labels={'x': 'Mountain Range', 'y': 'Height (m)'})
fig.update_layout(title=f'Highest Mountain in Each Mountain Range in {country}')
st.plotly_chart(fig)


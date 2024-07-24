import pandas as pd
import plotly.express as px
import streamlit as st

# Load the dataset
file_path = 'vehicles_us.csv'
df = pd.read_csv(file_path)

# Displaying basic information
st.header("Car Sales Data")
st.write("Data Overview:")
st.write(df.head())

st.write("Data Info:")
st.write(df.info())

st.write("Data Description:")
st.write(df.describe())

st.write("Missing Values:")
st.write(df.isnull().sum())

# Clean the dataset
df = df.dropna(subset=['model_year', 'cylinders', 'odometer'])
df['paint_color'] = df['paint_color'].fillna('Unknown')
df['is_4wd'] = df['is_4wd'].fillna(False)

# Showing cleaned data information
st.write("Cleaned Missing Values:")
st.write(df.isnull().sum())
st.write("Duplicate Rows:")
st.write(df.duplicated().sum())

# Plots
if st.checkbox('Show Model Year Distribution'):
    fig = px.histogram(df, x='model_year', title='Distribution of Car Model Years', nbins=100)
    st.plotly_chart(fig)

if st.checkbox('Show Price Distribution'):
    fig = px.histogram(df, x='price', title='Distribution of Car Prices', nbins=100)
    st.plotly_chart(fig)

if st.checkbox('Show Price vs. Car Type'):
    fig = px.scatter(df, x='type', y='price', title='Price vs. Car Type', color='type')
    st.plotly_chart(fig)

if st.checkbox('Show Price vs. Days Listed'):
    fig = px.scatter(df, x='days_listed', y='price', title='Price vs. Days Listed')
    st.plotly_chart(fig)

if st.checkbox('Show Fuel Type Distribution'):
    fuel_counts = df['fuel'].value_counts()
    fig = px.bar(fuel_counts, x=fuel_counts.index, y=fuel_counts.values, title='Count of Cars for Each Fuel Type')
    fig.update_layout(xaxis_title='Fuel Type', yaxis_title='Count of Cars')
    st.plotly_chart(fig)



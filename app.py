## app.py

# Import necessary libraries
import pandas as pd
import streamlit as st
import plotly.express as px

# Load dataset
car_data = pd.read_csv('vehicles_us.csv')

# Set header, title and author
st.header('Best-seller Cars dataframe')
st.title('Sprint 7 Project')
st.write('by: Tomas Orduna\n TripleTen Data Science student\n January 2025')

# ============================================================================

## Data Wrangling
car_data = car_data.dropna()
car_data['model_year'] = car_data['model_year'].astype(int)
car_data['date_posted'] = pd.to_datetime(car_data['date_posted'])

# Show data
car_data.info()
print()
car_data.describe()

# ============================================================================

# Set title
st.title('Sprint 7 Project')
st.write('by: Tomas Orduna, Data Science student')


# Histogram button creation
build_hist = st.checkbox('Generate histogram')

# Clicking the button
if build_hist:
        
    st.write('Histogram generator for the odometer in Vehicle Sells dataframe')     # Write the message   
    fig1 = px.histogram(car_data, x="odometer")  # Create histogram
    st.plotly_chart(fig1, use_container_width=True)  # Show an interactive Plotly graph


# Scatter button creation
scatter_button = st.button('Generate Scatter Plot')

# Clicking the button
if scatter_button:
    
    st.write('Scatter plot generator for the odometer and price in Vehicle Sells datafame')   # Write the message
    fig2 = px.scatter(car_data, x="odometer", y="price")    # Create scatter plot
    st.plotly_chart(fig2, use_container_width=True)     # Show an interactive Scatter plot


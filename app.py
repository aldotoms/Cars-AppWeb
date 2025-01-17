## app.py

# Import necessary libraries
import pandas as pd
import streamlit as st
import plotly.express as px

# Load dataset
df = pd.read_csv('vehicles_us.csv')

# Set header, title and author
st.title('BEST-SELLER Cars in USA Dataset')
st.header('Sprint 7 Project, DS-Tripleten Latam')
st.write('by: Tomas Orduna | Data Science student | Jan 2025')

# ============================================================================

## Data Wrangling
df = df.dropna()
df['model_year'] = df['model_year'].astype(int)
df['date_posted'] = pd.to_datetime(df['date_posted'])

# Show data
df.info()
print()
df.describe()
print()
df

# ============================================================================

# Description
st.write('In the following buttons, you can view the graphical information of the dataframe group by odometer and price.')


# Histogram button creation
build_histogram = st.checkbox('Generate Histogram')

# Clicking the button
if build_histogram:
        
    st.write('Histogram generator for the odometer in Vehicle Sells dataframe')     # Write the message   
    fig1 = px.histogram(df, x='odometer', color_discrete_sequence=['indianred'])  # Create histogram
    st.plotly_chart(fig1, use_container_width=True)  # Show an interactive Plotly graph

# ---------------------------------------------------------------------------------------------------

# Scatter button creation
scatter_button = st.button('View Scatter Plot')

# Clicking the button
if scatter_button:
    
    st.write('Scatter plot generator for the odometer and price in Vehicle Sells dataframe')   # Write the message
    fig2 = px.scatter(df, x='odometer', y='price')    # Create scatter plot
    st.plotly_chart(fig2, use_container_width=True)     # Show a Scatter plot

# ---------------------------------------------------------------------------------------------------

# Fuel bar creation
bar_button = st.button('Vreate a Bar Plot')

# Clicking the button
if bar_button:
    
    gb = df.groupby(['model_year', 'fuel'])['odometer'].mean().reset_index()
    fig3 = px.bar(gb, x="model_year", y="odometer", color="fuel", barmode="stack", title="Miles per Year model and Fuel type")
    st.plotly_chart(fig3, use_container_width=True)     # Show a Bar plot

# End.
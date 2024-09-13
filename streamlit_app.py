
import streamlit as st
import pandas as pd
import numpy as np

# Title of the web app
st.title('My First Streamlit App')

# Subheader
st.subheader('An example of simple data visualization')

# Create a simple dataframe
data = pd.DataFrame({
    'A': np.random.randn(50),
    'B': np.random.randn(50),
    'C': np.random.randn(50),
    'D': np.random.randn(50)
})

# Display the dataframe
st.write('Here is a random data sample:')
st.dataframe(data)

# Line chart for the dataframe
st.line_chart(data)

# Adding a slider for user interaction
st.write('Adjust the number of data points:')
num_points = st.slider('Number of points', min_value=10, max_value=100, value=50)

# Show filtered data based on the slider
filtered_data = data.head(num_points)
st.line_chart(filtered_data)

# Adding a button
if st.button('Click Me'):
    st.write('Button clicked!')

# Checkbox example
if st.checkbox('Show data'):
    st.write('Here is the data:')
    st.write(filtered_data)

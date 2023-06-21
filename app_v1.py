import streamlit as st
import pandas as pd
import plotly.express as px

# Load the watch dataset
df = pd.read_csv('watch_data.csv')

st.title("🕰️ Watch Market Insights")
st.write("""
Welcome to Watch Market Insights. Here you can explore market trends,
sales history, and compare watch brands. Navigate through the different
features to gain a deeper understanding of the watch market.
""")

# Exploratory Data Analysis
st.header("Exploratory Data Analysis")

# Display the first few rows of the data
st.subheader("Preview of Data")
st.write(df.head())

# Display the shape of the dataframe
st.subheader("Shape of the Data")
st.write(f"The dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")

# Display the different features in the data
st.subheader("Features in the Data")
st.write(df.columns.tolist())

# Display counts of each feature
st.subheader("Counts of Each Feature")
for column in df.columns:
    st.write(f"{column}: {df[column].nunique()} unique values")

# Filters in the sidebar
st.sidebar.title('Filters')
brand = st.sidebar.selectbox('Brand', options=df['Brand'].unique())
model = st.sidebar.selectbox('Model', options=df[df['Brand'] == brand]['Model'].unique())
min_price = st.sidebar.slider('Minimum Sold Price', min_value=int(df['Sold Price'].min()), max_value=int(df['Sold Price'].max()), value=int(df['Sold Price'].min()))
max_price = st.sidebar.slider('Maximum Sold Price', min_value=int(df['Sold Price'].min()), max_value=int(df['Sold Price'].max()), value=int(df['Sold Price'].max()))

# Filter dataframe
filtered_df = df[(df['Brand'] == brand) & (df['Model'] == model) & (df['Sold Price'] >= min_price) & (df['Sold Price'] <= max_price)]

st.header('Descriptive Analytics')
# Time-series plot for sold price
fig = px.line(filtered_df, x='Sale Date', y='Sold Price', title='Sold Price Over Time')
st.plotly_chart(fig)

# Scatter plot of Sold Price vs Listing Price
fig = px.scatter(filtered_df, x='Listing Price', y='Sold Price', color='Location', title='Sold Price vs Listing Price')
st.plotly_chart(fig)

# Display a table of sold prices
st.subheader('Sold Prices')
st.dataframe(filtered_df[['Reference Number', 'Sold Price', 'Sale Date']])

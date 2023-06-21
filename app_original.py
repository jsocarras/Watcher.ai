import streamlit as st
import requests

# Function to fetch watch data from eBay
def fetch_ebay_watch_data(reference_number):
    ebay_url = f"https://api.ebay.com/watches/{reference_number}"
    response = requests.get(ebay_url)
    data = response.json()
    return data

# Function to fetch watch data from Chrono24
def fetch_chrono24_watch_data(reference_number):
    chrono24_url = f"https://api.chrono24.com/watches/{reference_number}"
    response = requests.get(chrono24_url)
    data = response.json()
    return data

# Streamlit app
st.title("Watch Price Data")
st.write("Enter a watch reference number to fetch price data from eBay and Chrono24.")

reference_number = st.text_input("Watch Reference Number")

if st.button("Fetch Data"):
    if reference_number:
        # Fetch data from eBay
        ebay_data = fetch_ebay_watch_data(reference_number)
        st.subheader("eBay Watch Data")
        st.write(ebay_data)  # Display eBay data

        # Fetch data from Chrono24
        chrono24_data = fetch_chrono24_watch_data(reference_number)
        st.subheader("Chrono24 Watch Data")
        st.write(chrono24_data)  # Display Chrono24 data
    else:
        st.warning("Please enter a watch reference number.")

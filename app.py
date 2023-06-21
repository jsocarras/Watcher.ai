#app.py
import streamlit as st
import os
import shutil
import time
import threading
import pandas as pd
from scraper_watch import main as scrape_watch

def create_download_link(filename):
    with open(filename, "rb") as f:
        st.download_button(
            label="Download CSV",
            data=f,
            file_name="watch_listings.csv",
            mime="text/csv",
        )

def convert_price(price):
    price = price.replace(',', '')  # Remove the commas
    if ' to ' in price:
        low, high = price.split(' to ')
        return (float(low) + float(high)) / 2
    else:
        return float(price)

# Input field for watch name or model
watch_input = st.text_input("Enter watch name or model", "")

logo_path = 'img/watch.png'
st.image(logo_path, width=235)

st.title("Watcher.ai: Watch Listings Analytics")

st.markdown("Welcome to Watcher.ai's Watch Listings Analytics portal! Press the button below to scrape and export a list of current watch listings.")

if st.button("Analyze Watch Listings"):
    progress = st.progress(0)
    progress_pct = 0

    # Start a separate thread for the watch scraping
    def run_scrape():
        global progress_pct
        scrape_watch(watch_input)
        progress_pct = 100

    t = threading.Thread(target=run_scrape)
    t.start()

    # Update the progress bar in the main thread
    while progress_pct < 100:
        progress.progress(progress_pct)
        progress_pct += 2
        time.sleep(0.15)

    t.join()  # Wait for the scraping thread to complete

    # Check if watch_listings.csv exists before trying to load it
    if os.path.exists("watch_listings.csv"):
        # Load the scraped data
        data = pd.read_csv("watch_listings.csv")
        # Make sure 'price' column is numeric.
        data['price'] = data['price'].str.replace('$', '').apply(convert_price)

        # Display the data in a table
        st.dataframe(data)

        # Display some basic statistics
        st.markdown(f"Number of products: {len(data)}")
        st.markdown(f"Average price: ${data['price'].mean():.2f}")

        # Display a histogram of prices
        st.bar_chart(data['price'])

        create_download_link("watch_listings.csv")
    else:
        st.error("No listings found for the given watch model.")

# Watcher.ai: Watch Listings Analytics
Watcher.ai

## Overview
This Python application, using the Streamlit framework, enables you to scrape watch listing data from eBay. The application fetches current listings based on the name or model of a watch you input, and provides various statistics, such as the number of products and average price, as well as a histogram of prices. The scraped data can be downloaded as a CSV file.

## Prerequisites
- Python 3.7 or higher
- Streamlit
- Pandas
- BeautifulSoup
- Requests

These dependencies can be installed using pip:
```bash
pip install streamlit pandas beautifulsoup4 requests
```

## Code Structure
- app.py: This is the main file which runs the Streamlit application.
- scraper_watch.py: This file contains the functionality for scraping watch listing data from eBay.

## Downloading the Code
You can download the code by cloning this repository:
```bash
git clone <repository URL>
```

## Running the Application
Navigate into the directory where the application's code is located and run the following command:
```bash
streamlit run app.py
```

## How to Use
Open the application by visiting localhost:8501 in your web browser after running the command above.
Enter a watch name or model in the input field and press the "Analyze Watch Listings" button. The application will start scraping eBay for current watch listings.
Once the scraping process is complete, the application displays a table with the scraped data, provides some basic statistics, and shows a histogram of prices.
If you wish, you can download the scraped data as a CSV file by clicking the "Download CSV" button.

## Note
The scraping process may take some time depending on the number of listings found. Please be patient while the application is gathering data.

## Issues
If you encounter any issues or have any questions, please open an issue in this repository.

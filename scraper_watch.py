import requests
from bs4 import BeautifulSoup
import csv

def get_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup

# def parse_watch_listing(listing, watch_input):
#     title_tag = listing.find("h3", class_="s-item__title")
#     title = title_tag.text if title_tag else "N/A"
#
#     # Check if the title contains the watch name or model
#     if watch_input.lower() not in title.lower():
#         return None
#
#     price_tag = listing.find("span", class_="s-item__price")
#     price = price_tag.text if price_tag else "N/A"
#     url_tag = listing.find("a", class_="s-item__link")
#     url = url_tag["href"] if url_tag else "N/A"
#
#     return {
#         "title": title,
#         "price": price,
#         "url": url
#     }

def parse_watch_listing(listing, watch_input):
    title_tag = listing.find("div", class_="s-item__title").find("span")
    title = title_tag.text if title_tag else "N/A"

    # Check if the title contains the watch name or model
    if watch_input.lower() not in title.lower():
        return None

    price_tag = listing.find("span", class_="s-item__price")
    price = price_tag.text if price_tag else "N/A"
    url_tag = listing.find("a", class_="s-item__link")
    url = url_tag["href"] if url_tag else "N/A"

    return {
        "title": title,
        "price": price,
        "url": url
    }

def save_to_csv(listings, filename):
    keys = listings[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(listings)

def main(watch_input):
    print("watch input is: ", watch_input)
    if watch_input:
        watch_input_encoded = requests.utils.quote(watch_input)
        url = f"https://www.ebay.com/sch/i.html?_odkw={watch_input_encoded}&_sop=15&_nkw={watch_input_encoded}"
        listings = []
    else:
        url = "https://www.ebay.com/sch/i.html?_odkw=watches&_sop=15&_nkw=watches"
        listings = []

    soup = get_data(url)
    listings_list = soup.find_all("div", class_="s-item__info clearfix")

    for listing in listings_list:
        # Pass the watch_input to the parse_watch_listing function
        print("listing is: ", listing)
        print("watch_input is: ", watch_input)
        listing_data = parse_watch_listing(listing, watch_input)
        if listing_data is not None:
            listings.append(listing_data)

    if listings:
        save_to_csv(listings, "watch_listings.csv")

if __name__ == "__main__":
    main()

import pandas as pd
import requests
from bs4 import BeautifulSoup

Hotel = []
Description = []
Prices = []

# Iterate over pages from 1 to 15
for page_number in range(1, 16):
    url = f"https://www.airbnb.co.in/s/Jaipur--India/homes?adults=1&place_id=ChIJgeJXTN9KbDkRCS7yDDrG4Qw&refinement_paths%5B%5D=%2Fhomes&page={page_number}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    np = soup.find("a", class_="l1ovpqvx c1ytbx3a dir dir-ltr").get("href")
    cnp = "https://www.airbnb.co.in/" + np
    url = cnp
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    hotel_name = soup.find_all("div", class_="t1jojoys dir dir-ltr")
    hotel_prices = soup.find_all("div", class_="_1jo4hgw")
    hotel_desc = soup.find_all("div", class_="fb4nyux s1cjsi4j sgdvnt3 dir dir-ltr")

    # Ensure lists have the same length
    min_length = min(len(hotel_name), len(hotel_prices), len(hotel_desc))
    Hotel.extend([i.text for i in hotel_name[:min_length]])
    Prices.extend([i.text for i in hotel_prices[:min_length]])
    Description.extend([i.text for i in hotel_desc[:min_length]])

# Create DataFrame
df = pd.DataFrame({"Hotel Name": Hotel, "Description": Description, "Prices": Prices})

# Save DataFrame to CSV file with utf-8 encoding and 'replace' error handling
df.to_csv("airbnb_dat.csv", index=False, encoding="utf-8", errors="replace")






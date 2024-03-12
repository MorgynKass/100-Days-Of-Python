import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://www.amazon.com/dp/B0BNKZSHQ7/?coliid=I1GW3WOSOD1QBB&colid=3O3ZP7FIHL68&psc=1&ref_=list_c_wl_lv_ov_lig_dp_it"

HEADERS = {
    "User-Agent": "Defined",
    "Accept-Language": "en-US,en;q=0.9,la;q=0.8",
}

response = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price_with_dollar_sign = soup.find("span", class_="a-offscreen").getText()
price = price_with_dollar_sign.split("$")[1]
print(price_with_dollar_sign)

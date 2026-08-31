import sys
import requests
from bs4 import BeautifulSoup

def scrape_products(search_term):
    url = "https://mdcomputers.in/"
    params = {
        "route": "product/search",
        "search": search_term
    }

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, params=params, headers=headers, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    products = []

    for product in soup.select(".product-thumb"):
        name = product.select_one(".name")
        price = product.select_one(".price")
        link = product.select_one("a")

        if name:
            products.append({
                "name": name.get_text(" ", strip=True),
                "price": price.get_text(" ", strip=True) if price else "N/A",
                "url": link.get("href") if link else "N/A"
            })

    return products


if __name__ == "__main__":
    search_term = sys.argv[1] if len(sys.argv) > 1 else "laptop"

    try:
        products = scrape_products(search_term)

        for product in products:
            print(f"Product: {product['name']}")
            print(f"Price: {product['price']}")
            print(f"URL: {product['url']}")
            print("-" * 50)

    except Exception as e:
        print(f"Error: {e}")

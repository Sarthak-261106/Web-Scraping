import requests
from bs4 import BeautifulSoup
import os

product_urls = [
    "https://www.amazon.in/dp/B0G81TPT89",
    "https://www.amazon.in/dp/B0DGJ7TGDR"
]
target_price = float(input("Enter target price in ₹: "))

headers = {
    "User-Agent": "Mozilla/5.0"
}

for url in product_urls:

    print("\n" + "-" * 60)
    print("Product URL:", url)

    try:

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        # Parse webpage
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract product title
        title = soup.find(id="productTitle")

        if title:
            title = title.get_text(strip=True)
        else:
            title = "Title not found"

        # Extract product price
        price_tag = soup.select_one(
            "span.a-price span.a-offscreen"
        )

        if price_tag:
            price_text = price_tag.get_text(strip=True)

            # Remove ₹ and commas
            price = float(
                price_text.replace("₹", "").replace(",", "")
            )
        else:
            price = None

        # Extract product image URL
        image_tag = soup.find(id="landingImage")

        if image_tag:
            image_url = image_tag.get("src")
        else:
            image_url = None

        # Display product details
        print("Title:", title)

        if price is not None:
            print("Price: ₹", price)
        else:
            print("Price: Not found")

        print("Image URL:", image_url)

        # Compare price with target price
        if price is not None:

            if price < target_price:
                print("Price is below the target price.")

            elif price > target_price:
                print("Price is above the target price.")

            else:
                print("Price is equal to the target price.")

        # Download product image
        if image_url:

            image_response = requests.get(
                image_url,
                headers=headers,
                timeout=10
            )

            image_response.raise_for_status()

            os.makedirs("product_images", exist_ok=True)

            image_name = (
                "product_images/"
                + title[:30].replace("/", "_")
                + ".jpg"
            )

            with open(image_name, "wb") as image_file:
                image_file.write(image_response.content)

            print("Image downloaded successfully.")

    except requests.RequestException as error:

        print("Could not fetch the webpage.")
        print("Error:", error)

    except (ValueError, TypeError):

        print("Could not read the product price.")
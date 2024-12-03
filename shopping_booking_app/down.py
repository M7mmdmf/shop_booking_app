import os
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

# List of luxury brands
brands = [
    "Chanel", "Louis Vuitton", "Gucci", "Hermès", "Prada",
    "Dior", "Versace", "Fendi", "Dolce & Gabbana", "Burberry",
    "Armani", "Balenciaga", "Bottega Veneta", "Cartier", "Givenchy",
    "Valentino", "Yves Saint Laurent", "Rolex", "Tiffany & Co.", "Loro Piana",
    "Michael Kors", "Tom Ford", "Salvatore Ferragamo", "Bvlgari", "Hugo Boss",
    "Lacoste", "Ralph Lauren", "Alexander McQueen", "Jimmy Choo", "Chopard"
]

# Output directory for resized logos
output_dir = "assets/logos/"
os.makedirs(output_dir, exist_ok=True)

# Headers to mimic a browser request
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def fetch_image(brand):
    """
    Searches Google Images and fetches the first image result for a given brand.
    """
    search_url = f"https://www.google.com/search?q={brand}+logo&tbm=isch"
    try:
        response = requests.get(search_url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        img_tag = soup.find("img")
        img_url = img_tag["src"]

        # Download the image
        img_response = requests.get(img_url, headers=HEADERS, timeout=10)
        img_response.raise_for_status()
        return Image.open(BytesIO(img_response.content))
    except Exception as e:
        print(f"Error fetching image for {brand}: {e}")
        return None

def resize_and_save_image(image, brand):
    """
    Resizes the image to 20x20 and saves it as PNG.
    """
    resized_image = image.resize((20, 20), Image.ANTIALIAS)
    output_path = os.path.join(output_dir, f"{brand}.png")
    resized_image.save(output_path, "PNG")
    print(f"Saved {brand} logo to {output_path}")

# Process each brand
for brand in brands:
    print(f"Processing {brand}...")
    image = fetch_image(brand)
    if image:
        resize_and_save_image(image, brand)
    else:
        print(f"Failed to process {brand}.")

print("All logos processed.")

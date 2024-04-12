import requests
import csv
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Function to make API call and check if product exists
def check_product_exists(product_name):
    secret_token = os.getenv("SECRET_TOKEN")
    url = f"https://data.g2.com/api/v1/products/?filter[name]={product_name}"
    headers = {"Authorization": f"Bearer {secret_token}"}
    response = requests.get(url, headers=headers)
    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        # Check if the product name is a substring of any product name in the data
        for product in data['data']:
            if (product_name.casefold() in product['attributes']['name'].casefold()) or (product_name.casefold() in product['attributes']['short_name'].casefold()):
                return product
    return None

# Function to write product data to CSV
def write_to_csv(product, csv_file):
    # Check if the file is empty to write headers
    if os.path.exists(csv_file) == 0:
        with open(csv_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Name', 'Type', 'URL']) # Write header
    # Append data
    with open(csv_file, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([product['id'], product['attributes']['name'], product['attributes']['product_type'], product['attributes']['product_url']])

# Function to write not found products to CSV
def write_not_found_to_csv(product_name, csv_file):
    # Check if the file is empty to write headers
    if os.path.exists(csv_file) == 0:
        with open(csv_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Product Name']) # Write header for not found products
    # Append data
    with open(csv_file, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([product_name])

# Main script
if __name__ == "__main__":
    # File containing product names
    input_file = 'scraped_items.txt'
    # Output CSV file for found products
    output_file = 'products_found.csv'
    # Output CSV file for not found products
    not_found_file = 'products_not_found.csv'
    
    # Read each line from the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            product_name = line.strip() # Remove newline characters
            product = check_product_exists(product_name)
            if product:
                write_to_csv(product, output_file)
                print(f"Product '{product_name}' found and added to CSV.")
            else:
                write_not_found_to_csv(product_name, not_found_file) # Pass the file path as a string
                print(f"Product '{product_name}' not found.")
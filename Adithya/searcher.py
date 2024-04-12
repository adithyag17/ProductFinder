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
    if response.status_code == 200:
        data = response.json()
        # Check if the product name exists in the data
        for product in data['data']:
            if product['attributes']['name'] == product_name:
                return product
    return None

# Function to write product data to CSV
def write_to_csv(product, csv_file):
    with open(csv_file, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([product['id'], product['attributes']['name'], product['attributes']['product_type'], product['attributes']['product_url']])

# Function to write not found products to CSV
def write_not_found_to_csv(product_name, csv_file):
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
    
    # Open the CSV file for writing found products
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Name', 'Type', 'URL']) # Write header
        
        # Open the CSV file for writing not found products
        with open(not_found_file, 'w', newline='', encoding='utf-8') as not_found_file:
            writer = csv.writer(not_found_file)
            writer.writerow(['Product Name']) # Write header for not found products
        
        # Read each line from the input file
        with open(input_file, 'r', encoding='utf-8') as f:
            for line in f:
                product_name = line.strip() # Remove newline characters
                product = check_product_exists(product_name)
                if product:
                    write_to_csv(product, output_file)
                    print(f"Product '{product_name}' found and added to CSV.")
                else:
                    write_not_found_to_csv(product_name, not_found_file)
                    print(f"Product '{product_name}' not found.")

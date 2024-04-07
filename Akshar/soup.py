import mechanicalsoup

# Initialize a MechanicalSoup browser
browser = mechanicalsoup.StatefulBrowser()

# Define the URL of the TrustRadius categories page
url = 'https://www.trustradius.com/categories'

# Open the URL
browser.open(url)

# Get the page content
page = browser.get_current_page()

# Find the unordered list containing all the product categories
ul = page.find('ul', class_='link-list-columns')

# Find all the product categories
categories = ul.find_all('a')

# Create a file to save the product names and URLs
with open('trustradius_products.txt', 'w') as file:
    for category in categories:
        print(category)
        category_name = category.text.strip()
        category_url = category['href']
        
        # Navigate to the category URL
        browser.open("https://www.trustradius.com"+category_url)
        category_page = browser.get_current_page()
        
        # Find all the products in the category
        products = category_page.find_all('h3', class_='CategoryProduct_card-product-title__hhfnd')
        
        # Write the category name to the file
        file.write(f"{category_name}:\n")
        
        # Write the product names and URLs to the file
        for product in products:
            print(product)
            product_name = product.text.strip()
            product_url = product.find('a')['href']
            file.write(f"    {product_name}: {product_url}\n")

print("Data has been saved to trustradius_products.txt")

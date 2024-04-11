import mechanicalsoup

# Initialize a MechanicalSoup browser
browser = mechanicalsoup.StatefulBrowser()

# Define the URL of the TrustRadius categories page
main_url = 'https://www.trustradius.com'

url_suffix=['/categories','/education','/customer-support','/development','/enterprise','/finance-and-accounting','/human-resources','/information-technology','/marketing','/professional-services','/sales','/security','/vertical-specific','/']

categories=[]

# Open the URL
for suffix in url_suffix:
    url=browser.open(main_url+suffix)

    page = browser.get_current_page()


    ul = page.find('ul', class_='link-list-columns')

    # Find all the product categories
    if(ul):
        categories.append(ul.find_all('a'))

# Create a file to save the product names and URLs
product_set=set()

with open("trustradius_products.txt", 'w') as file:
    for category_list in categories:
        for category in category_list:
            print(category)
            category_name = category.text.strip()
            category_url = category['href']
            
            # Navigate to the category URL
            for i in range(0,500,25):
                browser.open(f"https://www.trustradius.com{category_url}?f={i}")
                category_page = browser.get_current_page()
                
                # Find all the products in the category
                products = category_page.find_all('h3', class_='CategoryProduct_card-product-title__hhfnd')
                print(len(products))
                
                # Write the category name to the file
                file.write(f"{category_name}:\n")
                
                # Write the product names and URLs to the file
                for product in products:
                    # print(product)
                    product_name = product.text.strip()
                    product_url = product.find('a')['href']
                    file.write(f"    {product_name}: {product_url}\n")
                    product_set.add(product_name)
                    # print(product_name)

with open('filtered_trustradius_products.txt', 'w') as file:
    for product in product_set:
        file.write(product.lower()+"\n")

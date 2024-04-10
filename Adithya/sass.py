import mechanicalsoup
import time

# Initialize a MechanicalSoup browser
browser = mechanicalsoup.StatefulBrowser()

# Define the URL of the TrustRadius categories page
url = 'https://www.saasworthy.com/list'

# Open the URL
browser.open(url)

# Get the page content
page = browser.get_current_page()

# List to store category URLs and their corresponding numbers
category_info = {}

# Find all <a> tags with href starting with '/list'
for link in page.find_all('a', href=lambda href: href and href.startswith('/list')):
    # Find the <span> element with class "catgry_no" inside the <a> tag
    span_element = link.find('span', class_='catgry_no')
    if span_element:
        # Extract the URL and number, then add them to the dictionary
        href = link.get('href')
        number_text = span_element.text.strip()
        # Remove brackets from the number_text and convert it to an integer
        number = int(number_text.replace('(', '').replace(')', ''))
        category_info[href] = number


print(category_info)

allprod = []
for urls, nums in category_info.items():
    iteratorval = nums // 20
    for i in range(1, iteratorval + 1):
        # Modify the URL with the page number
        modified_url = f'https://www.saasworthy.com{urls}?page={i}'
        b = browser.open(modified_url)
        prodpage = browser.get_current_page()
        if prodpage :
            try:
                products = prodpage.find_all('a', class_='decor-none blue')
                allprod.append(products)
                with open("sass_results.txt", "w",encoding="utf-8") as file:
                    for products_list in allprod:
                        for product in products_list:
                            extracted_word = product.text.split("What is")[1].strip()
                            extracted_word = extracted_word.split()[0]
                            file.write(str(extracted_word) + '\n')
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            break
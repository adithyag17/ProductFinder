from selenium import webdriver

file_path = "webcorpus.txt"
websites = []
updated_websites = []

# Read URLs from file and add them to the list
with open(file_path, 'r') as file:
    for line in file:
        website = line.strip()
        websites.append(website)

# Initialize the Chrome webdriver
driver = webdriver.Chrome()
# Loop through each website in the list
for website in websites:
    driver.get(website)
    # Find anchor elements on the webpage
    elements = driver.find_elements_by_tag_name('a')
    for element in elements:
        href = element.get_attribute('href')
        if href:  # Check if href attribute is not empty
            updated_url = f'{website} ({href})'
            print(updated_url)
            updated_websites.append(updated_url)

# Close the webdriver
driver.quit()

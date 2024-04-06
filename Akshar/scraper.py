from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urlparse, urljoin

file_path = "webcorpus.txt"
websites = []
scraped_urls = set()

# Read URLs from file and add them to the list
with open(file_path, 'r') as file:
    for line in file:
        website = line.strip()
        websites.append(website)

# Initialize the Chrome webdriver
driver = webdriver.Chrome()

def scrape_website(url, depth=1, max_depth=3):
    if depth > max_depth:
        return
    if url in scraped_urls:
        return
    
    print(f"Scraping: {url}")
    
    driver.get(url)
    
    # Find anchor elements on the webpage
    elements = driver.find_elements(By.TAG_NAME, 'a')
    
    for element in elements:
        href = element.get_attribute('href')
        if href:
            # Convert relative URLs to absolute URLs
            href = urljoin(url, href)
            
            # Check if the URL belongs to the same domain
            parsed_href = urlparse(href)
            parsed_url = urlparse(url)
            
            if parsed_href.netloc == parsed_url.netloc:
                scraped_urls.add(href)
                
                with open("scrapability_results.txt", "a") as file:
                    file.write(f"{url} ({href})\n")
                
                # Recursively scrape the new URL
                scrape_website(href, depth+1, max_depth)

for website in websites:
    scrape_website(website)

# Close the webdriver
driver.quit()

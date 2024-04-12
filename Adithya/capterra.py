from selenium import webdriver
from selenium.common.exceptions import WebDriverException, NoSuchElementException, StaleElementReferenceException
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
import time
#from fake_useragent import UserAgent
#options = Options()
#ua = UserAgent()
#user_agent = ua.random
#print(user_agent)
#options.add_argument(f'--user-agent={user_agent}')
driver = webdriver.Chrome()
def scrape_and_update_urls(file_path):
    
    
    updated_websites = []
    # Read URLs from file and add them to the list
    with open(file_path, 'r') as file:
        for line in file:
            website = line.strip()
            updated_websites.append(website)
    # Loop through each website in the list
    url_count = 0
    for website in updated_websites:
        try:
            driver.get(website)
            # Find anchor elements on the webpage with specific attributes
            elements = driver.find_elements_by_css_selector('a[href][class="sb color-mode-light link block font-bold no-underline"]')
            for element in elements:
                try:
                    href = element.get_attribute('href')
                    if href:  # Check if href attribute is not empty
                        print(href)
                        updated_websites.append(href)
                except StaleElementReferenceException:
                    print("StaleElementReferenceException: Element is stale, retrying...")
                    # You can add retry logic here or continue with the next element
                    continue
        except WebDriverException as e:
            print(f"WebDriverException occurred while processing website '{website}': {e}")

    # Print the total number of URLs processed
    #print(f"Total number of URLs processed: {url_count}")

    # Close the webdriver
    driver.quit()
    return updated_websites



def scrape_each_page(url):
    product_names = []
    
    try:
        driver.get(url)
        # Find the p element with class GlpyCExOomJSszk and id QTphXkFaGNDbpkg
        p_element = driver.find_element_by_css_selector('p.GlpyCExOomJSszk#QTphXkFaGNDbpkg')
        
        # Press and hold the button for 10 seconds
        actions = ActionChains(driver)
        actions.click_and_hold(p_element).perform()
        time.sleep(10)  # Wait for 10 seconds
        
        # Find product name elements on the webpage
        names = driver.find_elements_by_class_name('text-primary-80 leading-lg inline-flex items-center text-lg font-bold')  # Assuming this is the class name for product names
        product_names = [name.text.strip() for name in names if name.text.strip()]
        print(names)
        return product_names
    except StaleElementReferenceException:
        print("StaleElementReferenceException: Element is stale, retrying...")
        # You can add retry logic here or continue with the next element
    except NoSuchElementException:
        print(f"No product names found on the page: {url}")
        return []
    except WebDriverException as e:
        print(f"WebDriverException occurred while processing URL '{url}': {e}")
        return []
    finally:
        # Close the webdriver
        driver.quit()


def scrape_each_category(updated_urls):
    products = []
    for url in updated_urls:
        for i in range(2, 25):  # Adjust the range as needed
            pgurl = f'{url}?page={i}'
            names = scrape_each_page(pgurl)
            time.sleep(15) 
            if names:
                products.insert(names)
                print(names)
            else:
                print("ouy")
                break
             # Add this line to wait 15 seconds between each page
    return products

file_path = "webcorpus.txt"
updated_urls = scrape_and_update_urls(file_path)
final_products = scrape_each_category(updated_urls)
print(final_products)

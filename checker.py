import requests
from urllib.parse import urljoin

def can_scrape(url):
    robots_url = urljoin(url, "/robots.txt")
    try:
        response = requests.get(robots_url)
        if response.status_code == 200:
            return "Disallow:" not in response.text
        else:
            return True  # If unable to fetch robots.txt, assume it's allowed
    except requests.RequestException:
        return True  # If there's an error, assume it's allowed

# Example usage
url_to_scrape = "https://example.com"
if can_scrape(url_to_scrape):
    print("You can scrape this URL.")
else:
    print("You cannot scrape this URL.")

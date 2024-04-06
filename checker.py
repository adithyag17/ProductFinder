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

# List of URLs to check for scrapability
urls_to_check = [
    "https://www.capterra.com/360-degree-feedback-software/",
    "https://www.example.com",
    "https://www.somewebsite.com",
    # Add more URLs as needed
]

# Open a file to write the results
with open("scrapability_results.txt", "w") as file:
    for url in urls_to_check:
        if can_scrape(url):
            file.write(f"{url}: You can scrape this URL.\n")
        else:
            file.write(f"{url}: You cannot scrape this URL.\n")

print("Scrapability check completed. Results saved to scrapability_results.txt.")
